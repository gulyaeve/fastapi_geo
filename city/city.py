from fastapi import APIRouter, status
from city.schemas import City
from city.redis_client import add_city


router = APIRouter(prefix="/city")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_city(city: City):
    await add_city(city)

