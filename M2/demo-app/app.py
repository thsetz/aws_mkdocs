#!/usr/bin/env python3

import aws_cdk as cdk
from demo_app.demo_app_stack import DemoAppStack

app = cdk.App()
DemoAppStack(app, "demo-app")

app.synth()
