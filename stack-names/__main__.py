import os
import aws_cdk as cdk
from aws_cdk import aws_sqs as sqs


def main():
    app = cdk.App()
    env = cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    )

    prefix = app.node.try_get_context("prefix") or "quicktip-stack-name"

    stack1 = cdk.Stack(app, "stack1", env=env)
    stack2 = cdk.Stack(app, "stack2", stack_name=f"{prefix}-stack", env=env)

    sqs.Queue(stack1, "queue", visibility_timeout=cdk.Duration.seconds(300))
    sqs.Queue(stack2, "queue", visibility_timeout=cdk.Duration.seconds(300))

    app.synth()


if __name__ == "__main__":
    main()
