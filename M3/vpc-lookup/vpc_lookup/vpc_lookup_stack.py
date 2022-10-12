import aws_cdk as cdk
from constructs import Construct


class VpcLookupStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # We get the vpcid via context
        # - cdk [ls/deplox/init/..] -c vpcid=xxxx
        # -edit cdk.json
        #   add "vpcid": "THE_VALUEXXXX" to
        # "context": {}
        vpc_id = self.node.try_get_context("vpcid")
        # vpc = cdk.aws_ec2.Vpc.from_lookup(self, "VPC", is_default=True)
        vpc = cdk.aws_ec2.Vpc.from_lookup(self, "VPC", vpc_id=vpc_id)

        subnets = vpc.select_subnets(subnet_type=cdk.aws_ec2.SubnetType.PUBLIC)

        cdk.CfnOutput(self, "publicSubnets", value=str(subnets.subnet_ids))
