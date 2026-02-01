from fastapi import HTTPException, UploadFile, status
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import StreamingResponse

from src.api.storage.service import StorageService
from src.schemas.files import FilePath


class FilesService:
    @staticmethod
    async def upload(file: UploadFile, bot_id: str, user_id: str) -> FilePath:
        file_path = await run_in_threadpool(StorageService.upload, file=file, bot_id=bot_id, user_id=user_id)
        if not file_path:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File wasn't upload")
        return FilePath(file_path=file_path)

    @staticmethod
    async def get(image_path: str) -> StreamingResponse:
        body = await run_in_threadpool(StorageService.get, image_path=image_path)
        if not body:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="File wasn't fount")
        file = StreamingResponse(content=body, media_type='image/png')
        return file
