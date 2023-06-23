import boto3

# client representing DynamoDB
dynamodb_client=boto3.client('dynamodb')

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Create DynamoDB table.
mytable = dynamodb.create_table(
    TableName='employees',
    KeySchema=[
        {
            'AttributeName': 'empname',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'designation',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'empname',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'designation',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
mytable.wait_until_exists()

# Print out data about the table.
print("Below is table_status: ")
print(mytable.table_status)


items = [
    {'empname': 'Aman', 'designation': 'Manager'},
    {'empname': 'Abhinav', 'designation': 'Technical Architect'},
]


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

print("DONE!")

