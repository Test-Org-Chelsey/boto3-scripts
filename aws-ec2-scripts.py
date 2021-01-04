from secrets import python_access_key, python_secret_key
from pprint import pprint

import boto3

session = boto3.session.Session(aws_access_key_id=python_access_key,
                                aws_secret_access_key=python_secret_key)

ec2_resource = session.resource(service_name="ec2", region_name="us-east-2")

client = session.client(service_name="ec2", region_name="us-east-2")

# print('// List of all EC2 instances:')
# for ec2Instance in ec2_resource.instances.all():
#     print ec2Instance
# print ec2Instance.id

# print('// List out all possible operations for EC2 instances:')
# for ec2Instance in ec2_resource.instances.all():
#     pprint(dir(ec2Instance))
#     break

print('Information about EC2 Instances:')
for ec2Instance in ec2_resource.instances.all():
    ID = ec2Instance.instance_id
    print 'Instance id: ', ID
    Type = ec2Instance.instance_type
    print 'Instance Type: ', Type
    Architecture = ec2Instance.architecture
    print 'Instance Architecture: ', Architecture
    Hibernation = ec2Instance.hibernation_options
    print 'Hibernation options', Hibernation
    Volumes = ec2Instance.volumes
    print 'Volumes: ', Volumes
    VPC = ec2Instance.vpc
    print 'VPC: ', VPC
    State = ec2Instance.state
    print 'State: ', State
    print('// ----------- //')

# Stop a specific EC2 instance

# stopInstance = client.stop_instances(
#     InstanceIds=[
#         'i-0043d934d90df609d',
#     ],
# )


# start a specific EC2 instance:

# startInstance = client.start_instances(
#     InstanceIds=[
#         'i-0043d934d90df609d',
#     ],
# )
