from redis import Redis
from settings import settings


cache = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)