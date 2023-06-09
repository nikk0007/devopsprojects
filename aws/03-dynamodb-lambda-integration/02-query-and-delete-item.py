#!/usr/bin/env python3.9
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('employees')

# this is the lambda function
def lambda_handler(event, context): 
    response = table.query(
        KeyConditionExpression=Key('empname').eq('Aman') 
    )
    items = response['Items'][0]
    responses = table.delete_item(
        Key=items
        )
    list_items=str(responses)
    print("Deleting: " + list_items)