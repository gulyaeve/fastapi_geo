from redis.asyncio import Redis
from geo.schemas import City
import logging

cache = Redis()


async def add_city(city: City):
    await cache.geoadd("cities", city.get())
