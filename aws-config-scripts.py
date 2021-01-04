from secrets import python_access_key, python_secret_key
from pprint import pprint
import boto3

session = boto3.session.Session(aws_access_key_id=python_access_key,
                                aws_secret_access_key=python_secret_key)

client = boto3.client('config')

# client = session.client(service_name="config", region_name="us-east-2")

# describes the config rules
# description = client.describe_config_rules(
#     ConfigRuleNames=[
#         'string',
#     ],
#     NextToken='string'
# )

# triggers the evaluation of the set of the given set of rules
startEvaluation = client.start_config_rules_evaluation(
    ConfigRuleNames=[
        'required-tags',
    ]
)

response = client.describe_config_rules(
    ConfigRuleNames=[
        'required-tags',
    ],
)

print 'response', response

describeAggregateCompliance = client.describe_aggregate_compliance_by_config_rules(
    ConfigurationAggregatorName='string',
    Limit=0,
)

print 'Aggregate Compliance By Config Rule:', describeAggregateCompliance
