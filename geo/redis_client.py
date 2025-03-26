from redis.asyncio import Redis
from schemas import City, Coordinates

redis = Redis()


async def add_city(city: City):
    await redis.geoadd("cities", [city.get()])


async def get_city(city_name: str) -> Coordinates | None:
    coords = await redis.geopos("cities", city_name)
    if not coords or not coords[0]:
        return None
    longitude, latitude = coords[0]
    return Coordinates(latitude=latitude, longitude=longitude)
