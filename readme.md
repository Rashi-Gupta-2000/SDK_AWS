The project is a website that can access certain AWS services, with some of its features. There are seperate py files for a few of the services like ec2, s3, dynamoDB which are connected using Boto API. The routes or the backend files have only been created for the ec2 service. And the frontend has been implemented using bootstrap. When clicking on the button of a service on the home it takes us to create an instance and later we see the list of instances with some of its attributes and can be stopped,terminated or started.

First install aws cli and configure it
Then make the python files using boto
and use flask for backend and bootstrap for frontend 
Next we get a git url a docker hub url where the image has been pushed and a public ip address of the ec2 instance

sudo docker run -it --name new_cont0 -p 5000:5000 -e AWS_ACCESS_KEY_ID="" -e AWS_SECRET_ACCESS_KEY="" -e AWS_DEFAULT_REGION=us-east-1 rashig00/sdk:7.0

