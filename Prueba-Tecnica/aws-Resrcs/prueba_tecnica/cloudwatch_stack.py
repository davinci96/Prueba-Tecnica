from aws_cdk import Stack
from aws_cdk import aws_cloudwatch as cloudwatch
from aws_cdk import aws_ecs as ecs
from constructs import Construct

class CloudWatchStack(Stack):
    def __init__(self, scope: Construct, id: str, ecs_service: ecs.FargateService, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Crear una métrica para monitorear el uso de CPU de la ECS Service
        cpu_utilization_metric = ecs_service.metric_cpu_utilization(
            statistic="Average"
        )

        # Crear una alarma para la métrica de uso de CPU
        cpu_alarm = cloudwatch.Alarm(self, "CpuAlarm",
            metric=cpu_utilization_metric,
            threshold=70,  # Umbral del 70% de uso de CPU
            evaluation_periods=2,
            datapoints_to_alarm=2,
            alarm_description="Alarma de uso de CPU para el servicio ECS",
            actions_enabled=True  # Configura acciones como enviar notificaciones
        )

        # Crear un dashboard de CloudWatch
        dashboard = cloudwatch.Dashboard(self, "EcsDashboard")

        # Agregar un widget al dashboard para la métrica de uso de CPU
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="ECS CPU Utilization",
                left=[cpu_utilization_metric]
            )
        )

        # Agregar un widget al dashboard para mostrar el estado de la alarma
        dashboard.add_widgets(
            cloudwatch.AlarmWidget(
                title="CPU Alarm Status",
                alarm=cpu_alarm
            )
        )
