import boto3
from botocore.config import Config

from src.settings import settings

_session = boto3.Session(
    aws_access_key_id=settings.MINIO_ROOT_USER,
    aws_secret_access_key=settings.MINIO_ROOT_PASSWORD,
    region_name='us-east-1',
)


minio_client = _session.client(
    service_name='s3',
    endpoint_url=settings.MINIO_API_URL,
    config=Config(
        max_pool_connections=settings.MINIO_MAX_POOL_CONNECTIONS,
        retries={'max_attempts': settings.MINIO_RETRY_ATTEMPTS},
    ),
)
