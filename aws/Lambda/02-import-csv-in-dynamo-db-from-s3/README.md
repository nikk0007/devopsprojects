import CSV into DynamoDB using Lambda and S3 Event triggers.

Lambda role should have AmazonDynamoDBFullAccess and AmazonS3FullAccess policies.
The python code above does the following:

Imports the CSV file from S3 bucket.
Splits the CSV data into multiple strings.
Uploads data to the DynamoDB table.

Use Lambda template: Amazon S3 Put
enter s3 ARN and key name in Event Json.

Add Event Triggers to the S3 Bucket > Properties > Event Notifications
select suffix as .csv and Destination as Lambda function.

Now try to add another CSV file to S3 bucket. This will tigger an event and new data will also be added to dynamo db.