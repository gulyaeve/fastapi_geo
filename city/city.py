from typing import Literal

from fastapi import APIRouter, status, HTTPException
from schemas import City, Coordinates, Distance
from redis_client import add_city, get_city, get_distance

router = APIRouter(prefix="/city")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_city(city: City):
    await add_city(city)


@router.get("/{city_name}", response_model=Coordinates, responses={
    404: {"description": "City not found"},
    500: {"description": "Invalid coordinates format"}
})
async def get_city_coordinates(city_name: str):
    city_data = await get_city(city_name)

    if not city_data:
        raise HTTPException(status_code=404, detail="City not found")

    if None in [city_data.latitude, city_data.longitude]:
        raise HTTPException(status_code=500,
                            detail="Invalid coordinates format")

    return city_data


@router.get("/distance/{city1}/{city2}", response_model=Distance, responses={
    404: {"description": "One or both cities not found"},
    400: {"description": "Invalid unit parameter"}
})
async def calculate_distance(
        city1: str,
        city2: str,
        unit: Literal["m", "km", "mi", "ft"] = "km"
):
    if unit not in ["m", "km", "mi", "ft"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid unit. Allowed values: m, km, mi, ft"
        )

    distance = await get_distance(city1, city2, unit)

    if not distance:
        raise HTTPException(
            status_code=404,
            detail="One or both cities not found in database"
        )

    return distance
