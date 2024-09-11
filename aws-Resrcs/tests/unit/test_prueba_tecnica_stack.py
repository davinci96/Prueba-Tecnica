import aws_cdk as core
import aws_cdk.assertions as assertions

from prueba_tecnica.prueba_tecnica_stack import PruebaTecnicaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in prueba_tecnica/prueba_tecnica_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PruebaTecnicaStack(app, "prueba-tecnica")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
