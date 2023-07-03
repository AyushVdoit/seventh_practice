import aws_cdk as core
import aws_cdk.assertions as assertions

from seventh_practice.seventh_practice_stack import SeventhPracticeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in seventh_practice/seventh_practice_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SeventhPracticeStack(app, "seventh-practice")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
