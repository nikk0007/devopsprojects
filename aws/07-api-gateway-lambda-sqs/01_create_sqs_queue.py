import boto3

sqs_client=boto3.client("sqs")
sqs_resource = boto3.resource('sqs')

sqs_queue = sqs_resource.create_queue(QueueName='my_demo_queue')

# prints Standard Queue url
print('URL of Standard Queue created: ' + sqs_queue.url)