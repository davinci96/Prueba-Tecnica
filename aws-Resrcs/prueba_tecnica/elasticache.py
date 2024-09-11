from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_elasticache as elasticache
from constructs import Construct


class CacheStack(Stack):
    def __init__(self, scope: Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Crear un Security Group para Redis
        security_group = ec2.SecurityGroup(self, "RedisSecurityGroup",
            vpc=vpc,
            description="Allow access to Redis from ECS",
            allow_all_outbound=True
        )

        # Permitir tráfico hacia Redis (puerto 6379)
        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(6379),
            description="Allow traffic to Redis"
        )

        # Crear un grupo de subredes de ElastiCache con las subredes de la VPC proporcionada
        subnet_group = elasticache.CfnSubnetGroup(self, "RedisSubnetGroup",
            description="Subnet group for ElastiCache Redis",
            subnet_ids=[subnet.subnet_id for subnet in vpc.private_subnets]  # Utilizar subredes privadas
        )

        # Configuración de ElastiCache Redis con el grupo de subredes personalizado
        self.cache = elasticache.CfnCacheCluster(self, "RedisCache",
            cache_node_type="cache.t3.micro",
            num_cache_nodes=1,
            engine="redis",
            vpc_security_group_ids=[security_group.security_group_id],
            cache_subnet_group_name=subnet_group.ref  # Asignar el grupo de subredes creado
        )

        # Endpoint del Redis para conectar desde ECS u otros servicios
        self.redis_endpoint = self.cache.attr_redis_endpoint_address
