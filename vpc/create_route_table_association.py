import boto3

route_table_id = 'rtb-0b9e8988e338d4dab'
subnet_id = 'subnet-0256d880d0680f490'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association["AssociationId"])