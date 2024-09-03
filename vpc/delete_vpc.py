import boto3

vpc_id = "vpc-032e7c847cdcb663d"

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)