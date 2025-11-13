import boto3
import os
import json
import urllib.parse

# AWS clients
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
sns = boto3.client('sns', region_name=os.environ.get('REGION', 'eu-north-1'))

# Environment variables
SNS_ARN = os.environ.get('SNS_ARN', 'arn:aws:sns:eu-north-1:658855380670:AI-Rekognito')
BUCKET_NAME = os.environ.get('BUCKET_NAME', 'user-uploaded-images-ai')
MAX_LABELS = int(os.environ.get('MAX_LABELS', 5))
MIN_CONFIDENCE = int(os.environ.get('MIN_CONFIDENCE', 80))
REGION = os.environ.get('REGION', 'eu-north-1')

def lambda_handler(event, context):
    try:
        # Check if event has S3 Records
        if 'Records' not in event:
            return {
                'statusCode': 400,
                'body': json.dumps('No S3 event detected. Please test with a proper S3 event.')
            }

        # Extract S3 info
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])

        print(f"Processing image: {key} from bucket: {bucket}")

        # Detect labels with Rekognition
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=MAX_LABELS,
            MinConfidence=MIN_CONFIDENCE
        )

        # Extract labels
        labels = [label['Name'] for label in response['Labels']]
        description = f"Your uploaded image '{key}' contains: {', '.join(labels)}."

        # Generate S3 URL for the image
        image_url = f"https://{bucket}.s3.{REGION}.amazonaws.com/{key}"
        full_message = f"{description}\n\nView your image here: {image_url}"

        print(f"Detected labels: {labels}")
        print(f"Publishing to SNS topic: {SNS_ARN}")

        # Publish to SNS
        sns_response = sns.publish(
            TopicArn=SNS_ARN,
            Message=full_message,
            Subject='Image Analysis Result'
        )

        print(f"SNS message ID: {sns_response['MessageId']}")

        return {
            'statusCode': 200,
            'body': json.dumps('SNS notification sent successfully!')
        }

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {str(e)}")
        }
