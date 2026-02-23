#  Serverless Magic with AWS Rekognition  
### Automated Image Analysis System using S3, Lambda, SNS & Rekognition

##  About The Project

This project demonstrates a **fully serverless AI-powered image recognition system** built using AWS cloud services.

Whenever a user uploads an image to an Amazon S3 bucket:

1. The upload event automatically triggers an AWS Lambda function.
2. The Lambda function calls AWS Rekognition to analyze the image.
3. Rekognition detects labels and confidence scores.
4. The results are sent to users via Amazon SNS (email notification).

This system requires **no servers to manage**, making it scalable, cost-effective, and production-ready.

---
---
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-Serverless-orange?logo=awslambda)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-Storage-red?logo=amazons3)
![AWS Rekognition](https://img.shields.io/badge/AWS%20Rekognition-Image%20AI-blue?logo=amazonaws)
![Amazon SNS](https://img.shields.io/badge/Amazon%20SNS-Notifications-purple?logo=amazon)
![AWS IAM](https://img.shields.io/badge/AWS%20IAM-Security-yellow?logo=amazon)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-green?logo=serverless)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Region](https://img.shields.io/badge/Region-ap--south--1%20(Mumbai)-teal?logo=amazonaws)
![Automation](https://img.shields.io/badge/Trigger-S3%20Event%20Driven-lightgrey?logo=amazon)
![License](https://img.shields.io/badge/License-MIT-lightgreen?logo=openai)

## 🚀 Features

- Automatic image analysis using AWS Rekognition  
- Event-driven architecture using S3 triggers  
- Email notifications via SNS  
- Secure IAM role-based access  
- Configurable environment variables  
- Fully serverless architecture  
- Python 3.12 runtime  

---

## 🧩 Architecture Overview

### Workflow

1. User uploads an image (.jpg, .png, etc.) to S3
2. S3 triggers the Lambda function
3. Lambda sends the image to AWS Rekognition
4. Rekognition detects labels and confidence levels
5. Lambda publishes the results to SNS
6. SNS sends email notification to subscribed users

---

## 🛠️ Tech Stack

| Service | Purpose |
|----------|----------|
| Amazon S3 | Stores uploaded images |
| AWS Lambda | Executes backend logic automatically |
| AWS Rekognition | Performs image analysis |
| Amazon SNS | Sends notification emails |
| AWS IAM | Handles permissions and security |
| Python 3.12 | Lambda runtime language |

---

# ⚙️ Step-by-Step Setup Guide (Beginner Friendly)

## Step 1: Create S3 Bucket

1. Go to AWS Console  
2. Open S3  
3. Click "Create Bucket"  
4. Bucket name: `user-uploaded-images-ai`  
5. Select Region: **ap-south-1 (Mumbai)**  
6. Keep default settings and create bucket  

---

## Step 2: Create SNS Topic

1. Open SNS service  
2. Click "Create Topic"  
3. Select Standard  
4. Topic name: `AI-Rekognito`  
5. Create topic  
6. Copy the Topic ARN  

### Create Email Subscription

1. Open the topic  
2. Click "Create Subscription"  
3. Protocol: Email  
4. Enter your email address  
5. Confirm subscription from your inbox  

---

## Step 3: Create IAM Role for Lambda

1. Open IAM  
2. Click Roles → Create Role  
3. Select AWS Service  
4. Choose Lambda  
5. Attach the following policies:

- AmazonS3ReadOnlyAccess  
- AmazonRekognitionFullAccess  
- AmazonSNSFullAccess  
- AWSLambdaBasicExecutionRole  

6. Name the role: `Lambda-Rekognition-Role`  
7. Create role  

---

## Step 4: Create Lambda Function

1. Open AWS Lambda  
2. Click "Create Function"  
3. Select "Author from scratch"  

### Basic Configuration

- Function name: `ImageAnalysisFunction`
- Runtime: Python 3.12
- Architecture: x86_64
- Execution Role: Use existing role
- Select: `Lambda-Rekognition-Role`

Click "Create Function"

---

## Step 5: Add Environment Variables

Go to:

Lambda → Configuration → Environment Variables → Edit

Add:

| Key | Value |
|-----|--------|
| BUCKET_NAME | user-uploaded-images-ai |
| MAX_LABELS | 5 |
| MIN_CONFIDENCE | 80 |
| REGION | ap-south-1 |
| SNS_ARN | arn:aws:sns:ap-south-1:<YOUR_ACCOUNT_ID>:AI-Rekognito |

Save changes.

---

## Step 6: Upload Lambda Code

Replace the default Lambda code with your project Python file from this repository.

Deploy the function.

---

## Step 7: Add S3 Trigger

1. Open Lambda function  
2. Go to Configuration → Triggers  
3. Click "Add Trigger"  
4. Select S3  
5. Choose bucket: `user-uploaded-images-ai`  
6. Event type: All object create events  
7. Add trigger  

Now your Lambda will automatically execute when a new image is uploaded.

---

## Step 8: Test the System

1. Go to S3  
2. Upload any image file  
3. Wait a few seconds  
4. Check your email  

You will receive detected labels and confidence scores.

---

## 🌍 Region Configuration

Region used: **ap-south-1 (Mumbai)**  

Note: AWS Rekognition must be available in the selected region.

---

## 🔐 Security Notes

- Use least privilege IAM permissions in production
- Restrict S3 bucket public access
- Validate file types before processing
- Monitor Lambda logs in CloudWatch

---

## 📂 Clone Repository

```bash
git clone https://github.com/Shivamgarud8/images-Rekognito.git
cd images-Rekognito
