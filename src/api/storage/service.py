from uuid import uuid4

from fastapi import UploadFile

from src.api.storage.client import minio_client
from src.schemas.files import FileInfo
from src.settings import settings


class StorageService:
    @staticmethod
    def upload(file: UploadFile, bot_id: str, user_id: str) -> FileInfo:
        ext = file.filename.split('.')[-1]
        key = f'{bot_id}/{user_id}/{uuid4()}.{ext}'

        minio_client.upload_fileobj(
            Fileobj=file.file,
            Bucket=settings.MINIO_BUCKET,
            Key=key,
            ExtraArgs={'ContentType': file.content_type},
        )

        return FileInfo(uuid=key)

    @staticmethod
    def get_presigned_url(image_path: str) -> str:
        return minio_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': settings.MINIO_BUCKET,
                'Key': image_path,
            },
            ExpiresIn=settings.MINIO_PRESIGNED_URL_EXPIRES_IN,
        )
