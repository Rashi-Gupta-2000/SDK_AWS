import boto3

#Function for connecting to EC2 
ec2 = boto3.client('ec2',
                    'us-east-1',
                    aws_access_key_id='',
                    aws_secret_access_key='')  # enter access key details

def create_instances(image_id,mincount,maxcount,instance_type):
    #Function for running instances 
    conn = ec2.run_instances(InstanceType=instance_type,
                             MaxCount=maxcount,
                             MinCount=mincount,
                             ImageId=image_id)
    # print(conn)

# ids = ['i-04c0aa876baf792ed']

def list_instances():
    #This function will describe all the instances
    #with their current state 

    # conn = boto3.resource('ec2')
    # instances = conn.instances.filter()
    # for instance in instances:
    #     if instance.state["Name"] == "running":
    #         return instance.id

    # ec2 = boto3.client("ec2")
    # reservations = ec2.describe_instances(Filters=[
    #     {
    #         "Name": "instance-state-name",
    #         "Values": ["running"]
    #     }
    # ]).get("Reservations")

    # return reservations

    # l = list()

    # for r in reservations:
    #     for i in r['Instances']:
    #         id = i['InstanceId']
    #         l.append(id)
    # return l
    
    res = ec2.describe_instances().get("Reservations")
    return res
    # res = ec2.describe_instance_status()
    # return res

def stop_instances(ids):
    ec2.stop_instances(InstanceIds=[ids])

def start_instances(ids):
    ec2.start_instances(InstanceIds=[ids])

def terminate_instances(ids):
    ec2.terminate_instances(InstanceIds=[ids])

def describe_key():
    keypairs = ec2.describe_key_pairs()
# print(keypairs)
