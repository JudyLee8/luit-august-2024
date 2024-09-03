import boto3

route_table_id = "rtb-01501afb8dd70dc52"
internet_gateway_id = "igw-0c7fd924b1d2f42b3"

ec2 = boto3.client('ec2')

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)