from aws_cdk import Stack
from aws_cdk import aws_ecs as ecs
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ecr as ecr
from constructs import Construct

class EcsStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, ecr_repository1: ecr.Repository, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.cluster = ecs.Cluster(self, "EcsCluster", vpc=vpc)

        # Primer servicio ECS
        task_definition1 = ecs.FargateTaskDefinition(self, "TaskDef1")
        task_definition1.add_container("AppContainer1",
            image=ecs.ContainerImage.from_ecr_repository(ecr_repository1, tag="latest"),
            memory_limit_mib=512,
            cpu=256,
            port_mappings=[ecs.PortMapping(container_port=5000)]
        )

        self.service1 = ecs.FargateService(self, "FargateService1",
            cluster=self.cluster,
            task_definition=task_definition1,
            desired_count=1
        )

        scaling1 = self.service1.auto_scale_task_count(
            min_capacity=1,
            max_capacity=3
        )
        scaling1.scale_on_cpu_utilization(
            "CpuScaling1",
            target_utilization_percent=50
        )
