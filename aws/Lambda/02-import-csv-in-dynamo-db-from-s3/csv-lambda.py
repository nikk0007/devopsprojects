import boto3
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("employees")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    Employees = data.split("\n")
    #print(Employees)
    for employee in Employees:
        print(employee)
        employee_data = employee.split(",")
        # add to dynamodb
        try:
            table.put_item(
                Item = {
                    "id"        : employee_data[0],
                    "name"      : employee_data[1],
                    "Subject"   : employee_data[2]
                }
            )
        except Exception as e:
            print("End of file")
