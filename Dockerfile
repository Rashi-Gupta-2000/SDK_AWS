FROM python:latest
COPY . /app
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install 
# enter access key details
# RUN aws configure set region us-east-1 
# RUN aws configure set aws_access_key_id 
# RUN aws configure set aws_secret_access_key 

RUN aws configure set output json
WORKDIR /app
RUN pip install flask
RUN pip install boto3

EXPOSE 5000

CMD [ "python3", "routes.py" ]