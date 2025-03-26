from fastapi import APIRouter
from geo.schemas import City
from geo.redis_client import add_city


router = APIRouter(prefix="/geo")


@router.post("/")
async def create_city(city: City):
    await add_city(city)
    return city
