from redis.asyncio import Redis
from geo.schemas import City, CityDist

cache = Redis()


async def add_city(city: City):
    await cache.geoadd("cities", city.get())


async def get_all_cities() -> list[City]:
    names = await cache.zrange("cities", 0, -1)
    coords = await cache.geopos("cities", *names)

    result = []
    for name, coord in zip(names, coords):
        result.append(City(name=name, longitude=coord[0], latitude=coord[1]))

    return result


async def get_city(name: str) -> City | None:
    if not (coords := await cache.geopos("cities", name)) or not coords[0]:
        return None

    return City(
        name=name,
        longitude=coords[0][0],
        latitude=coords[0][1],
    )


async def get_distance(city1: str, city2: str, unit: str = "km") -> CityDist | None:
    if unit not in ["m", "km", "mi", "ft"]:
        return None

    if not await cache.zscore("cities", city1):
        return None

    if not await cache.zscore("cities", city2):
        return None

    distance = await cache.geodist("cities", city1, city2, unit=unit)

    if distance is None:
        return None

    return CityDist(city1=city1, city2=city2, dist=distance, unit=unit)
