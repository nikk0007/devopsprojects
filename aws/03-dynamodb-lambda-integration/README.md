Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale

Here we have four python files to create, add data, query and delete the dynamoDB table.
To execute these on CLI, we must first configure AWS CLI with credentials using the below command:
- aws configure

Create an IAM role and attach AWS Managed AmazonDynamoDBFullAccess and AWSLambdaBasicExecutionRole policies.
Lambda will require these roles to access DynamoDB.