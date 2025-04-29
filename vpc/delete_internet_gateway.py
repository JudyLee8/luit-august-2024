import boto3

internet_gateway_id = "igw-0c7fd924b1d2f42b3"

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)