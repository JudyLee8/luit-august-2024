import boto3

internet_gateway_id = "igw-0c7fd924b1d2f42b3"
vpc_id = "vpc-032e7c847cdcb663d"

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)