from fastapi import FastAPI
from geo.geo import router as geo_router


app = FastAPI()

app.include_router(geo_router)


@app.get("/")
async def get_root():
    return {"Hello": "World"}

