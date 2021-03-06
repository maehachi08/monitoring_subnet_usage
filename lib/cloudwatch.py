import boto3

client = boto3.client('cloudwatch')


def put_metric_data_wrapper(
        subnet_id: str,
        available_ip_address_count: int
):
    response = client.put_metric_data(
        Namespace='VPC/Subnet',
        MetricData=[
            {
                'MetricName': 'available_ip_address_count',
                'Dimensions': [
                    {
                        'Name': 'subnetId',
                        'Value': subnet_id
                    },
                ],
                'Value': available_ip_address_count,
                'Unit': 'Count',
            },
        ]
    )

    return response
