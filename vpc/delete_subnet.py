import boto3

subnet_id = "subnet-0256d880d0680f490"

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)