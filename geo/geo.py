from fastapi import APIRouter, HTTPException, status
from geo.schemas import City, CityDist
from geo.redis_client import (
    add_city,
    get_city as get_city_redis,
    get_all_cities,
    get_distance as get_distance_redis,
)


router = APIRouter(prefix="/geo")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_city(city: City):
    await add_city(city)


@router.get("/{name}", response_model=City)
async def get_city(name: str):
    if (response := await get_city_redis(name)) is None:
        raise HTTPException(status_code=404, detail="City not found")

    return response


@router.get("/", response_model=list[City])
async def get_cities():
    return await get_all_cities()


@router.get("/distance/{city1}/{city2}", response_model=CityDist)
async def get_distance(city1: str, city2: str, unit: str = "km"):
    return await get_distance_redis(city1, city2, unit)
