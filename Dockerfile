FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos y la aplicación
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Exponer el puerto que Flask usará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
