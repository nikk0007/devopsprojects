import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    now = datetime.now()
    time_date = now.strftime("%H:%M:%S %m/%d/%Y")
    sqs = boto3.client('sqs')
    #sqs.send_message(QueueUrl="https://sqs.us-east-1.amazonaws.com/xxxxxxxxxxxx/time_queue",MessageBody=time_date)
    sqs.send_message(QueueUrl="https://sqs.us-east-1.amazonaws.com/xxxxxxxxxxxx/time_queue",MessageBody=time_date)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Message sent Successfully!')
        
    }