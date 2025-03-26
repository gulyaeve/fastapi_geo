from fastapi import FastAPI
from city.city import router as geo_router
from fastapi_redis_cache import FastApiRedisCache, cache
from settings import settings
from time import sleep


app = FastAPI()

app.include_router(geo_router)


@app.on_event("startup")
def start():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=settings.redis_url,
        prefix="myapi-cache",
    )

@app.get("/")
async def get_root():
    return {"Hello": "World"}


# Не будет кэшировано
@app.get("/users")
async def get_users():
    sleep(1)
    return {"Users": {"name": "vasya"}}


# Будет кэшировано
@app.get("/users2")
@cache(expire=60)
async def get_users_2():
    sleep(1)
    return {"Users2": {"name": "vasya"}}