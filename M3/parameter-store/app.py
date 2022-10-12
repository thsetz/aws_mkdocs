#!/usr/bin/env python3
import os
import aws_cdk as cdk

from parameter_store.parameter_store_stack import ParameterStoreStack


app = cdk.App()
ParameterStoreStack(
    app,
    "parameter-store",
    env={
        "account": os.environ["CDK_DEFAULT_ACCOUNT"],
        "region": os.environ["CDK_DEFAULT_REGION"],
    },
)

app.synth()
