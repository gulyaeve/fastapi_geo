from redis.asyncio import Redis
from city.schemas import City
from settings import settings


cache = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)


async def add_city(city: City):
    await cache.geoadd("cities", city.get())
