from fastapi import APIRouter, UploadFile
from shutil import copyfileobj
from redis import Redis
from config import cache

# from utils.image import resize


router = APIRouter(prefix="/image")


@router.post("/")
async def add_image(name: str, file: UploadFile):
    image_path = f"temp/{name}.webp"
    with open(image_path, "wb+") as file_object:
        copyfileobj(file.file, file_object)
    # TODO: Обработка будет тут
    cache.publish("images", image_path)
    # resize(image_path)