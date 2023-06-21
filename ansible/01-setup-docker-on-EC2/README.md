#upgrade Ansible if required:
>pip install --upgrade ansible

>ansible-playbook -i inventory.yaml docker-playbook.yaml

#Type "yes" if it says that the authencity of the host can't be established and asks if we want to continue connecting.

#Docker will be installed. Can be tested using:
>docker ps
>docker run -d -p 81:80 nikk007/apachewebsite

#Now we can access the webpage using port 81 and public IP of EC2.



