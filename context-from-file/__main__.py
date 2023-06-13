import tomllib as toml
import aws_cdk as cdk

config_data = None
with open("config.toml", "rb") as f:
    config_data = toml.load(f)

app = cdk.App(context=config_data)

account = app.node.try_get_context("account")
region = app.node.try_get_context("region")
env = cdk.Environment(account=account, region=region)

deployment = app.node.try_get_context("deployment")
stack_name = f"{deployment['prefix']}-stack"
stack = cdk.Stack(app, "stack", stack_name=stack_name, env=env)

app.synth()
