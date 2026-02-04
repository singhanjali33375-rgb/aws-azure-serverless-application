# aws-azure-serverless-application
A serverless application demonstrating development and deployment using AWS Lambda and Azure Functions. The project showcases event-driven architecture, API integration, logging, and monitoring without managing servers.
# Serverless Application Development & Deployment

## 📌 Project Overview
This project demonstrates serverless application development using AWS Lambda and Azure Functions. It follows an event-driven architecture and eliminates server management while ensuring scalability and reliability.

## ☁️ Technologies Used
- AWS Lambda
- Amazon API Gateway
- Azure Functions
- CloudWatch & Azure Monitor
- Python

## 🏗️ Architecture
- Client sends request via API Gateway
- AWS Lambda / Azure Function processes request
- Logs stored in CloudWatch / Azure Monitor
- Serverless architecture ensures auto-scaling

## 📂 Project Structure
serverless-app-development-deployment/ ├── aws-lambda/ ├── azure-function/ ├── api/ ├── monitoring/ └── sample-events/
serverless-app-development-deployment/
│
├── README.md
│
├── aws-lambda/
│   ├── lambda_function.py
│   └── template.yaml
│
├── azure-function/
│   ├── __init__.py
│   └── function.json
│
├── api/
│   └── api-spec.yaml
│
├── monitoring/
│   └── logging.md
│
└── sample-events/
    └── event.json
    ## 🚀 Features
- Fully serverless backend
- Event-driven execution
- Auto-scaling and high availability
- Integrated logging and monitoring
- Cloud-agnostic design (AWS & Azure)

## 🧪 Sample Use Case
The application receives a request, processes data using a serverless function, and returns a response without provisioning servers.

## 📊 Monitoring & Logging
- AWS CloudWatch for Lambda logs
- Azure Monitor for Function logs

## 👤 Author
Anjali Singh
• Designed and documented a serverless application using AWS Lambda and Azure Functions.
• Implemented event-driven architecture with API Gateway.
• Demonstrated logging and monitoring using CloudWatch and Azure Monitor.
• Created cloud-agnostic serverless design for scalable applications.
“This project focuses on serverless application development using AWS Lambda and Azure Functions to build scalable, event-driven applications without server management.”
serverless-app-development-deployment/
│
├── terraform/
│   ├── provider.tf
│   ├── variables.tf
│   ├── lambda.tf
│   ├── api-gateway.tf
│   ├── outputs.tf
│
├── cicd/
│   └── github-actions.yml
## 🏗️ Infrastructure as Code (Terraform)

Terraform is used to provision AWS Lambda, IAM roles, and API Gateway.

### Steps:
1. terraform init
2. terraform plan
3. terraform apply
   ## 🔄 CI/CD Pipeline

This project uses GitHub Actions for CI/CD.

Pipeline Steps:
- Trigger on code push
- Package Lambda function
- Deploy infrastructure using Terraform
- Fully automated serverless deployment
-  • Implemented Infrastructure as Code using Terraform for AWS Lambda and API Gateway.
   • Designed CI/CD pipeline using GitHub Actions for automated deployment.
   • Automated serverless deployment with zero manual intervention.
   • Applied DevOps best practices with version-controlled infrastructure.
   I built a serverless application using AWS Lambda and Azure Functions. Infrastructure was provisioned using Terraform, and I implemented a CI/CD pipeline with GitHub Actions to automate build and deployment.”
