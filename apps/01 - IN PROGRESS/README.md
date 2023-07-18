



- k apply -f db-init-script-configmap.yaml
- k apply -f db-deployment.yaml
- k exec -it <db-pod-name> -- bash
- mysql -h localhost -u root -p
Enter the root password when prompted.
- SHOW DATABASES;
- USE emp_db;
- SHOW TABLES;
- select * from employees

- pip install mysql-connector-python
- pip install memcache