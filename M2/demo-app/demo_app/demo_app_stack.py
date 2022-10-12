import aws_cdk as cdk
from constructs import Construct


class DemoAppStack(cdk.Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        cdk.aws_s3.Bucket(self, "cdk-source-bucket")
