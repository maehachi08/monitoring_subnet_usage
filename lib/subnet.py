import boto3
import json

client = boto3.client('ec2')


def get_available_ip_address_count(subnet_ids: list):
    response = client.describe_subnets(
        SubnetIds=subnet_ids
    )

    # print(json.dumps(response, indent=4, sort_keys=True))
    for subnet in response['Subnets']:
        # print(json.dumps(subnet, indent=4, sort_keys=True))
        # print(subnet['SubnetId'] + ': ' + str(subnet['AvailableIpAddressCount']))
        return subnet['AvailableIpAddressCount']
