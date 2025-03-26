from redis import Redis
from settings import settings


cache = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)


if __name__ == "__main__":
    cities = cache.georadius("cities", 0, 0, 22000, "km")
    print(cities)