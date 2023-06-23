import boto3


# client representing DynamoDB
dynamodb_client=boto3.client('dynamodb')

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

items = [
    {'empname': 'Aman', 'designation': 'Manager'},
    {'empname': 'Abhinav', 'designation': 'Technical Architect'},
]

mytable = dynamodb.Table('employees') 

# using DynamoDB.Table.batch_writer() is used for a large of items
with mytable.batch_writer() as batch:
    for i in items:
        batch.put_item(    
        Item=i
        )

# adding item individually
mytable.put_item(
   Item={
        'empname': 'Prateek',
        'designation': 'Systems Engineer',
    }
)

# adding item individually
mytable.put_item(
   Item={
        'empname': 'Rohit',
        'designation': 'Resource Manager',
    }
)

print("DATA ADDED")

# Print attributes about the table.
print('Table ARN: ' + mytable.table_arn)
print('Table ID: ' + mytable.table_id)
print('Table Name: ' + mytable.table_name)
print('Table Status: ' + mytable.table_status)
