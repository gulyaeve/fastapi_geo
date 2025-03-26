from redis.asyncio import Redis
from geo.schemas import City

cache = Redis()


async def add_city(city: City):
    await cache.geoadd("cities", city.get())
