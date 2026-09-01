# 🛠️ AWS Serverless Tools

A monorepo of AWS serverless projects built with SAM & CloudFormation.
Maintained by [@Ryan-Adams57](https://github.com/Ryan-Adams57)

## 📁 Projects

| Project | Stack | Description |
|---|---|---|
| [static-website-hosting](./static-website-hosting) | S3 + CloudFront + Route 53 | Secure static website hosting |
| [serverless-todo-api](./serverless-todo-api) | Lambda + API Gateway + DynamoDB | Serverless REST API |
| [image-processing-pipeline](./image-processing-pipeline) | S3 + Lambda + DynamoDB | Auto image resize & metadata |
| [bulk-email-dispatcher](./bulk-email-dispatcher) | SES + SNS + EventBridge | Scheduled bulk email system |

## 🚀 Deployment

\`\`\`bash
cd <project-folder>
sam build
sam deploy --guided
\`\`\`
