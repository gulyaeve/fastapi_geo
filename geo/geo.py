from fastapi import APIRouter, status
from geo.schemas import City
from geo.redis_client import add_city


router = APIRouter(prefix="/geo")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_city(city: City):
    await add_city(city)

