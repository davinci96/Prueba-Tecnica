# Prueba Técnica

Repositorio que contiene prueba técnica para el cargo de Analista CloudOps :)

## Calculadora de Costos

[Calculadora de AWS](https://calculator.aws/#/estimate?id=ae60d126ed3f516df05e054ca7ab6a14ce6f305d)

## Diagrama de Arquitectura

![Diagrama de Arquitectura](https://github.com/user-attachments/assets/ba124cd3-0756-4171-8655-ed60ec7c6c19)

## Explicación del Pipeline y la Infraestructura

Este proyecto consta de dos partes:

### 1. Pipelines

El repositorio contiene un pipeline en la carpeta `.github/workflows/DeployInfra.yaml`, realizado con GitHub Actions. Se divide en dos pasos:

#### 1.1 DeployInfra2

- Configura AWS Credentials.
- Instala dependencias para CDK y otras herramientas.
- Bootstrap CDK para preparar el entorno.
- Despliega la infraestructura (VPC, ECR, DynamoDb, ElastiCache).
- Construye, etiqueta y sube imágenes Docker a Amazon ECR.

#### 1.2 Deploy-Ecs-Elb

- Despliega el ECS Stack, ELB y un Monitor de CloudWatch en el entorno de AWS, después de que DeployInfra2 se haya completado.

Se usa una estrategia de despliegue secuencial. Primero, se despliega la infraestructura base (VPC, repositorios de ECR, etc.), y luego, en un paso separado, se despliegan los servicios en ECS, ELB y CloudWatch que dependen de esa infraestructura.

### 2. Infraestructura como Código (IaC)

La infraestructura se encuentra en la ruta `aws-Resrcs` y utiliza AWS Cloud Development Kit (CDK). La infraestructura incluye:

- **VPC (Virtual Private Cloud)**

  Archivo: `vpc_stack.py`

  Define una VPC con subredes públicas y privadas. Utiliza un archivo de parámetros (`parameters.json`) para definir el CIDR y otros parámetros importantes.

- **ECS (Elastic Container Service)**

  Archivo: `ecs_stack.py`

  Crea un clúster de ECS con servicios Fargate. Incluye autoescalado de tareas basado en la utilización de CPU.

- **ECR (Elastic Container Registry)**

  Archivos: `ecr_stack.py` y `ecr_stack2.py`

  Define dos repositorios de ECR para almacenar imágenes de contenedor, configurados con reglas de ciclo de vida para mantener solo las imágenes etiquetadas como 'latest'.

- **ELB (Elastic Load Balancer)**

  Archivo: `elb_stack.py`

  Configura dos Application Load Balancers (ALB) para los servicios ECS. Cada ALB escucha en el puerto 80 (HTTP) y redirige el tráfico a los servicios ECS.

- **CloudWatch**

  Archivo: `cloudwatch_stack.py`

  Define una pila de AWS CDK para monitorear un servicio ECS utilizando CloudWatch. Incluye una métrica para el uso de CPU y una alarma que se activa si el uso supera el 70% durante dos períodos consecutivos.

- **DynamoDB**

  Archivo: `dynamodb_stack.py`

  Crea una tabla de DynamoDB con una clave de partición llamada `ID` de tipo string y utiliza el modo de facturación `PAY_PER_REQUEST`.

- **ElastiCache**

  Archivo: `elasticache.py`

  Configura un clúster de ElastiCache Redis dentro de una VPC existente, con un Security Group para Redis y un grupo de subredes privadas.

### Cómo Ejecutar

#### Localmente

1. **Configuración Inicial:**

   Asegúrate de tener AWS CLI y AWS CDK instalados y configurados.

2. **Bootstrap:**

   Ejecuta `cdk bootstrap` para inicializar los recursos necesarios en tu cuenta de AWS.

3. **Despliegue:**

   Ejecuta `cdk deploy` o `cdk deploy VpcStack`, `cdk deploy EcrStack`, etc., para desplegar la infraestructura.

#### Automáticamente

El pipeline se ejecuta automáticamente cuando se hace un commit en las ramas `develop`, `release` o `main`. El agente tiene los paquetes y librerías necesarios. La región de despliegue depende de la rama:

- `main`: us-east-2
- `release`: us-west-2
- `develop`: us-east-1

#### Requisitos

- AWS CLI
- AWS CDK
- Node.js
- Python 3.12

Además, crea secretos en Repository secrets para que el pipeline funcione correctamente:

- `AWS_ACCOUNT_ID`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`



