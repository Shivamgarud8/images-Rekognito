# 🧠 Serverless Magic with AWS Rekognition  
### Automated Image Analysis System using S3, Lambda, SNS & Rekognition

This project demonstrates a **fully serverless AI-powered image recognition system** built using AWS services.  
Whenever a user uploads an image to an **S3 bucket**, it **automatically triggers a Lambda function**, which uses **AWS Rekognition** to analyze the image and then sends the **detection details via SNS** (email notification).

---

## 🚀 Features

- 🖼️ **Automatic Image Analysis** using AWS Rekognition  
- 📦 **S3 Trigger Integration** – runs instantly when a new image is uploaded  
- 📤 **SNS Notifications** – sends analysis results directly to your email  
- 🔐 **IAM Role Configuration** – secure and permission-based access  
- ⚙️ **Environment Variables** for easy configuration without code changes  
- ☁️ **Completely Serverless** – no servers to manage or scale  

---

## 🧩 Architecture Overview

1. **S3 Bucket** → Uploads an image (`.jpg`, `.png`, etc.)  
2. **Lambda Function** → Automatically triggered  
3. **AWS Rekognition** → Analyzes the uploaded image  
4. **SNS Topic** → Sends results to subscribed users  

---

## 🛠️ Tech Stack

| Service | Purpose |
|----------|----------|
| **AWS S3** | Stores uploaded images |
| **AWS Lambda** | Executes image analysis automatically |
| **AWS Rekognition** | Detects labels, objects, and confidence |
| **AWS SNS** | Sends results as notifications |
| **AWS IAM** | Manages permissions and access control |

---

## ⚙️ Setup Guide

Follow the steps below to set up your own **Image Analysis System**:

###  Clone the Repository
```bash
git clone https://github.com/Shivamgarud8/images-Rekognito.git
cd images-Rekognito

```

###  Add Environment Variables

Add the following environment variables in your Lambda function configuration:

| Key | Value |
|-----|--------|
| **BUCKET_NAME** | user-uploaded-images-ai |
| **MAX_LABELS** | 5 |
| **MIN_CONFIDENCE** | 80 |
| **REGION** | ap-south-1 |
| **SNS_ARN** | arn:aws:sns:ap-south-1:<YOUR_ACCOUNT_ID>:AI-Rekognito |

> ⚠️ **Note:** Region updated to **Mumbai (ap-south-1)** due to AWS Rekognition service availability.

### 7️⃣ Add S3 Trigger

You can set up an S3 trigger for your Lambda function using the AWS Management Console or AWS CLI.


1. Navigate to your **Lambda Function** → **Configuration** → **Triggers**  
2. Click **Add Trigger**  
3. Select **S3** as the trigger source  
4. Choose your bucket → `user-uploaded-images-ai`  
5. Set **Event type** to `All object create events`  
6. Click **Add**

---


---
👩‍🏫 **Guided and Supported by [Trupti Mane Ma’am](https://github.com/iamtruptimane)**  
---

👨‍💻 **Developed By:**  
**Shivam Garud**  
🧠 *DevOps & Cloud Enthusiast*  
💼 *Automating deployments, one pipeline at a time!*  

## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/shivam-garud-371b5a307/)
[![Medium-blog](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://medium.com/@shivam.garud2011/serverless-magic-with-aws-rekognition-automated-image-analysis-system-c71f50b3c5d1/)

