from fastapi import HTTPException, UploadFile, status
from fastapi.concurrency import run_in_threadpool

from src.api.storage.service import StorageService
from src.schemas.files import FileInfo


class FilesService:
    @staticmethod
    async def upload(file: UploadFile, bot_id: str, user_id: str) -> FileInfo:
        file_uuid = await run_in_threadpool(StorageService.upload, file=file, bot_id=bot_id, user_id=user_id)
        if not file_uuid:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File wasn't upload")
        return file_uuid

    @staticmethod
    async def get_image_url(image_path: str) -> str:
        presigned_url = await run_in_threadpool(StorageService.get_presigned_url, image_path=image_path)
        if not presigned_url:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Presigned url wasn't generate")
        return presigned_url
