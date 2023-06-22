import boto3

dynamodb = boto3.client('dynamodb')


# delete the table movies
response = dynamodb.delete_table(
    TableName='employees'
)

print("--------------  TABLE DELETED  --------------")
