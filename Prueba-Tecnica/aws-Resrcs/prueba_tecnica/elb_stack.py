from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_elasticloadbalancingv2 as elbv2
from constructs import Construct
from aws_cdk import Duration

class ElbStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, ecs_service1: ecs.FargateService, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        alb1 = elbv2.ApplicationLoadBalancer(self, "ALB1",
            vpc=vpc,
            internet_facing=True
        )

        listener1 = alb1.add_listener("Listener1", port=80)

        # Configuración Target Group 
        target_group1 = elbv2.ApplicationTargetGroup(self, "TargetGroup1",
            vpc=vpc,
            port=5000, 
            protocol=elbv2.ApplicationProtocol.HTTP, 
            targets=[ecs_service1],
            health_check=elbv2.HealthCheck(
                path="/", 
                interval=Duration.seconds(30),
                timeout=Duration.seconds(5),
                healthy_http_codes="200"
            )
        )

        listener1.add_target_groups("TargetGroup1",
            target_groups=[target_group1]
        )

        self.alb1_dns = alb1.load_balancer_dns_name

