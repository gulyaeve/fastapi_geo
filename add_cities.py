import json
from redis import Redis
from settings import settings


cache = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

with open("russian-cities.json") as file:
    cities = json.loads(file.read())


for city in cities:
    # print(city, end="\n\n")
    data = (city['coords']['lon'], city['coords']['lat'], city['name'])
    print(data)
    cache.geoadd("cities", data)