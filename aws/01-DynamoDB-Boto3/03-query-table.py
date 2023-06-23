import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

# client representing DynamoDB
dynamodb_client=boto3.client('dynamodb')

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
mytable = dynamodb.Table('employees') 

# Query Table
# return the title Silsila
response = mytable.query(      
    KeyConditionExpression=Key('empname').eq('Prateek') 
)

items = response['Items']
print("Below is item corresponding to Prateek")
print(items)
print("---------------------------------------------------------")

# scan complete table
# scan the table
response = mytable.scan()
items = response['Items']
# print the items in the table
print("Below the result of scanning the complete table")
print(items)
print("---------------------------------------------------------")

# list ALL tables
tables = list(dynamodb.tables.all())
print("List of ALL tables: ")
print(tables)
print("---------------------------------------------------------")

# scan the table movies
response = dynamodb_client.scan(
    TableName='employees'  
    )

print("scan report in json format")
for i in response['Items']:  
    print(json.dumps(i))

print("---------------------------------------------------------")

# delete the item from the table
mytable.delete_item(
    Key={
        'empname': 'Aman',
        'designation': 'Manager'
    }
)

print("Deleted an item from the table")
print("---------------------------------------------------------")

# add new items to the table
# adding an item
mytable.put_item(
   Item={
        'empname': 'Nikhil',
        'designation': 'Asst. Manager'
    }
)

print("Added an item to the table")
print("---------------------------------------------------------")


