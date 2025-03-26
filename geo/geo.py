from fastapi import APIRouter, status, HTTPException
from schemas import City, Coordinates
from redis_client import add_city, get_city

router = APIRouter(prefix="/geo")


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
