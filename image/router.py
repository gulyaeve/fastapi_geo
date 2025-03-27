from fastapi import APIRouter, UploadFile
from shutil import copyfileobj


router = APIRouter(prefix="/image")


@router.post("/")
async def add_image(name: str, file: UploadFile):
    image_path = f"temp/{name}.webp"
    with open(image_path, "wb+") as file_object:
        copyfileobj(file.file, file_object)
    # TODO: Обработка будет тут