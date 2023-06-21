terraform init
terraform fmt
terraform validate
terraform plan
terraform apply --auto-approve


Goto MS Workbench and Click on the plus icon.:
Connection Name: MyDatabseConnection

Host Name: Enter the endpoint myrdsinstance.xoxoxoxoxo.us-east-1.rds.amazonaws.com

Port: 3306

Username: myrdsuser

Password: Click on Store in Vault and enter password myrdspassword. Click on ok.

Now click on Test Connection > OK
Now click on the DB connection to open the database.
After successfully connecting and opening the database, you can create tables and run queries.

Navigate to the Schemas tab to see databases available to start doing database operations. 


To delete the resources:
terraform destroy --auto-approve
