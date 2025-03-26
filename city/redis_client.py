from redis.asyncio import Redis
from city.schemas import City

cache = Redis()


async def add_city(city: City):
    await cache.geoadd("cities", city.get())
