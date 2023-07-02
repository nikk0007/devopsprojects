We will create two public EC2 instances. One for wordpress and another for mysql database.
For simplicity, we will keep both instances in public subnets and will use docker to install wordpress and mysql.

So first of all, we will create EC2 instances using terraform:
terraform init
terraform fmt
terraform validate
terraform apply --auto-approve

Then install docker in both of them using the playbook in ansible folder: we are using ad-hoc command for simplicity:
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -u ubuntu -i <WORDPRESS EC2 PUBLIC IP>,<MYSQL EC2 PUBLIC IP>, --private-key ../keys/mykey -e 'pub_key=../keys/mykey.pub' docker-playbook.yaml

You can visit here to check details of how to use Mysql container: https://hub.docker.com/_/mysql

run mysql container in mysql EC2:
- docker pull mysql:5.7
- docker run -d \
  --name mysql \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=<MySQL root password> \
  -e MYSQL_DATABASE=<WordPress database name> \
  -v ~/mysql_data:/var/lib/mysql \
  mysql:5.7

EXAMPLE:
docker run -d 
  --name mysql \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=pass \
  -e MYSQL_DATABASE=mydb \
  -v ~/mysql_data:/var/lib/mysql \
  mysql:5.7

To check mysql running container:
- docker exec -it mysql bash
- mysql -u root -p
- then enter password supplied ealier
# you can create a new database just for testing
- SHOW DATABASES;
- CREATE DATABASE my_wp_db;
- USE my_wp_db
- SHOW TABLES;



Then we have to run wordpress container inside wordpress EC2:
- docker pull wordpress
- docker run -d \
  --name wordpress \
  -p 80:80 \
  -e WORDPRESS_DB_HOST=<MySQL EC2 private IP> \
  -e WORDPRESS_DB_USER=<MySQL username> \
  -e WORDPRESS_DB_PASSWORD=<MySQL password> \
  -e WORDPRESS_DB_NAME=<WordPress database name> \
  -v ~/wordpress/wp-content:/var/www/html/wp-content \
  wordpress


EXAMPLE:
- docker run -d \
  --name wordpress \
  -p 80:80 \
  -e WORDPRESS_DB_HOST=172.31.29.194 \
  -e WORDPRESS_DB_USER=root \
  -e WORDPRESS_DB_PASSWORD=pass \
  -e WORDPRESS_DB_NAME=mydb \
  -v ~/wordpress/wp-content:/var/www/html/wp-content \
  wordpress


NOW you can access the wordpress in browser via public IP of wordpress EC2.
To destroy the infrastructure:
- terraform destroy --auto-approve

Now you can try on your own by placing the mysql database in a private subnet and createv a NAT gateway in public subnet to connect it to internet.
====================================================================

