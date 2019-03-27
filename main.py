import traceback
from botocore.exceptions import ClientError

import lib.enum as enum
import lib.subnet as subnet
import lib.ecs as ecs
import lib.cloudwatch as cloudwatch
import lib.pandas as pandas

'''
    subnet-id 1000 1030
1    subnet-AAAAAA    32    31
2    subnet-BBBBBB    32    25
'''

CSV_PATH = 'monitoring_subnet_usage.csv'


try:
    for subnet_id in enum.subnet_ids:
        available_ip_address_count = subnet.get_available_ip_address_count([subnet_id])
        put_metric_data_response = cloudwatch.put_metric_data_wrapper(subnet_id, available_ip_address_count)

except ClientError as e:
    print(traceback.format_exc())

