from aws_cdk import Stack
from aws_cdk import aws_dynamodb as dynamodb
from constructs import Construct
from aws_cdk import RemovalPolicy

class DynamoDbStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Configuración de DynamoDB
        self.table = dynamodb.Table(self, "Tabla de Pragma",
            partition_key=dynamodb.Attribute(name="ID", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )
