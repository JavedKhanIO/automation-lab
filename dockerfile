#use official python image
FROM python:3.12-slim
#setting working directory inside container
WORKDIR /app
#copying python script into container
COPY auto-hello.py .
COPY cpu-load.py .

#installing psutil
RUN pip install psutil

#commands to run when container runs
CMD ["python", "cpu-load.py"]

