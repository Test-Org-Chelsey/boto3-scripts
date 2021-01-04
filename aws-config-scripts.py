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
        'required-tags', 'cloudformation-stack-notification-check', 'iam-password-policy', 'cloud-trail-cloud-watch-logs-enabled', 'codepipeline-deployment-count-check', 'access-keys-rotated'
    ]
)

# response = client.describe_config_rules(
#     ConfigRuleNames=[
#         'required-tags', 'cloudformation-stack-notification-check', 'iam-password-policy', 'cloud-trail-cloud-watch-logs-enabled', 'codepipeline-deployment-count-check', 'access-keys-rotated'
#     ],
# )

# print 'response', response


# evaluationStatus = client.describe_config_rule_evaluation_status(
#     ConfigRuleNames=[
#         'required-tags', 'cloudformation-stack-notification-check', 'iam-password-policy', 'cloud-trail-cloud-watch-logs-enabled', 'codepipeline-deployment-count-check', 'access-keys-rotated'
#     ],
#     Limit=50
# )

# print 'EVALUATION STATUS: ', evaluationStatus
