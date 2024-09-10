# Descargar imagen de Ubuntu (Desde docker.hub)
FROM ubuntu:22.04

# Descargar la lista de manejo de paquetes
RUN apt-get update

# Actualzar la lista de paquetes
RUN apt-get upgrade -y

# Instalar el compilador o lenguaje que corre nuestro programa
RUN apt-get install python3 -y

# Copiar los archivos de la aplicación dentro del contenedor
COPY ./webpy /home/webpy

# Establecer el directorio de trabajo
WORKDIR /home/webpy

# Instalar el módulo pip
RUN apt-get install python3-pip -y

# Instalar requirements del proyecto
RUN pip3 install -r requirements.txt

# Abrir el puerto para la app web
EXPOSE 8080

# Ejecutar la aplicación web.py
CMD [ "python3", "app.py" ]