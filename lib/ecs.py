import boto3

client = boto3.client('ec2')


def get_available_ip_address_count(subnet_ids=None):
    response = client.describe_subnets(
        SubnetIds=subnet_ids
    )

