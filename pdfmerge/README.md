[![deploy](https://github.com/Sebas1012/pdfmerge/actions/workflows/PublishDockerImage.yml/badge.svg)](https://github.com/Sebas1012/pdfmerge/actions/workflows/PublishDockerImage.yml)

# MergePDF

MergePDF es un cliente web liviano desarrollado con Flask que simplifica la fusión de múltiples archivos PDF en uno solo. Con una interfaz sencilla y rápida, MergePDF ofrece una solución eficiente para combinar documentos PDF, facilitando la gestión de archivos de manera ágil y sin complicaciones..

<p align="center">
<img src="https://i.ibb.co/9vRXByp/2022-10-26-09-16-58-online-video-cutter-com.gif" alt="UI" border="0">
</p>

## Importante⚠️:

No olvides reemplazar en el [Dockerfile](Dockerfile) la variable de entorno `SECRET_KEY` con cualquier token generado por ti.

## Ejecutar con Docker:

Para ejecutar la aplicacion solo basta con ejecutar el siguiente comando:

```
docker run -p 80:5000 pdfmerger:latest
```

## Ejecutar con Python:

Para ejecutar con python primero deberiamos crear un entorno virtual he instalar las dependencias necesarias con el comando:

```
pip install -r requirements.txt
```

Luego podemos lanzar la app con el comando:

```
flask --app main.py run
```

## Dependencias:
| Libreria | Version |
| --- | --- |
| [PyPDF2](https://pypi.org/project/PyPDF2/)  | 2.11.1 |
| [Flask](https://flask.palletsprojects.com/en/2.2.x/) | 2.2.2 |
| [Werkzeug](https://werkzeug.palletsprojects.com/en/2.2.x/) | 2.2.2 |



<p align="center">
  <b>Hecho con &#10084; por: Sebastián. </b>
</p>
