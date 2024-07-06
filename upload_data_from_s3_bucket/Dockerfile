FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir boto3 python-dotenv
CMD ["python", "upload_data_s3_bucket.py"]
