from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from constructs import Construct
import json

class VpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        with open("finaktiva_cluster/parameters.json") as f:
            parameters = json.load(f)

        vpc_cidr = parameters.get("VpcCidr")
        private_subnet1_cidr = parameters.get("PrivateSubnet1Cidr")
        private_subnet2_cidr = parameters.get("PrivateSubnet2Cidr")

        if not vpc_cidr or not private_subnet1_cidr or not private_subnet2_cidr:
            raise ValueError("Missing required CIDR parameters in parameters.json")

        # VPC
        self.vpc = ec2.Vpc(self, "MyVpc",
            ip_addresses=ec2.IpAddresses.cidr(vpc_cidr),
            max_azs=3,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="PublicSubnet",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="PrivateSubnet1",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="PrivateSubnet2",
                    cidr_mask=24
                )
            ]
        )
