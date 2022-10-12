import aws_cdk as cdk
from constructs import Construct

# from aws_cdk import core, aws_ssm as ssm, aws_iam as iam


class ParameterStoreStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # To init: aws ssm put-parameter --name "string-parameter"
        #     --type "String" --value "this-is-a-string"
        # This method will pull a String from parameter store at deployment
        # That String is the token used .. (by Reference)
        string_param = cdk.aws.ssm.StringParameter.value_for_string_parameter(
            self, "string-parameter"
        )

        # This method will pull a String from parameter store at syhtnesis
        # That String is the the "REAL" Value (By Value)
        synth_string_param = cdk.aws.ssm.StringParameter.value_from_lookup(
            self, "string-parameter"
        )

        # This method will pull a SecretString that can
        # be used as a password in another resource
        secure_string_param = cdk.SecretValue.ssm_secure(
            "secure-parameter", "1"
        )  # noqa: E501

        cdk.aws_iam.User(self, "user", password=secure_string_param)

        cdk.CfnOutput(self, "deployment-parameter", value=string_param)
        cdk.CfnOutput(self, "synthesis-parameter", value=synth_string_param)
