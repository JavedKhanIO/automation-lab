FROM python:3.9-slim
WORKDIR /app
COPY webhealth.py .
RUN pip install --no-cache-dir flask requests
EXPOSE 5000
CMD ["python3", "webhealth.py"]
