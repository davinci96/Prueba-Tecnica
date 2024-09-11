from aws_cdk import App
from prueba_tecnica.ecs_stack import EcsStack
from prueba_tecnica.ecr_stack import EcrStack
from prueba_tecnica.vpc_stack import VpcStack
from prueba_tecnica.elb_stack import ElbStack
from prueba_tecnica.dynamodb_stack import DynamoDbStack
from prueba_tecnica.elasticache import CacheStack
from prueba_tecnica.cloudwatch_stack import CloudWatchStack


app = App()

# VPC
vpc_stack = VpcStack(app, "VpcStack")

# ECR
ecr_stack = EcrStack(app, "EcrStack")  

# ECS 
ecs_stack = EcsStack(app, "EcsStack", 
    vpc=vpc_stack.vpc, 
    ecr_repository1=ecr_stack.ecr_repository
)

# ELBs 
elb_stack = ElbStack(app, "ElbStack", 
    vpc=vpc_stack.vpc, 
    ecs_service1=ecs_stack.service1
)

# dynamodb
dynamodb_stack = DynamoDbStack(app, "DynamoDbStack")

# elasticache
elasticache = CacheStack(app, "CacheStack", vpc=vpc_stack.vpc)

#cloudwatch
CloudWatch = CloudWatchStack(app, "CloudWatchStack", ecs_service=ecs_stack.service1)

app.synth()