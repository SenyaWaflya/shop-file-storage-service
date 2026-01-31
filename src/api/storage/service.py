from uuid import uuid4

from botocore.response import StreamingBody
from fastapi import UploadFile

from src.api.storage.client import minio_client
from src.settings import settings


class StorageService:
    @staticmethod
    def upload(file: UploadFile, bot_id: str, user_id: str) -> str:
        ext = file.filename.split('.')[-1]
        key = f'{bot_id}/{user_id}/{uuid4()}.{ext}'

        minio_client.upload_fileobj(
            Fileobj=file.file,
            Bucket=settings.MINIO_BUCKET,
            Key=key,
            ExtraArgs={'ContentType': file.content_type},
        )
        return key

    @staticmethod
    def get(image_path: str) -> StreamingBody:
        response = minio_client.get_object(
            Bucket=settings.MINIO_BUCKET,
            Key=image_path,
        )
        return response['Body']
