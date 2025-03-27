from typing import Literal

from redis.asyncio import Redis
from schemas import City, Distance, Coordinates

redis = Redis()


async def add_city(city: City):
    await redis.geoadd("cities", [city.get()])


async def get_city(city_name: str) -> Coordinates | None:
    coords = await redis.geopos("cities", city_name)
    if not coords or not coords[0]:
        return None
    longitude, latitude = coords[0]
    return Coordinates(latitude=latitude, longitude=longitude)


async def get_distance(city1: str, city2: str, unit: Literal[
        "m", "km", "mi", "ft"] = "km") -> Distance | None:
    valid_units = ["m", "km", "mi", "ft"]
    if unit not in valid_units:
        raise ValueError(f"Invalid unit. Allowed: {valid_units}")

    distance = await redis.geodist("cities", city1, city2, unit)
    if distance is None:
        return None

    return Distance(
        city_from=city1,
        city_to=city2,
        distance=round(float(distance), 2),
        unit=unit
    )
