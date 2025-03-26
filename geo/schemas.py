from pydantic import BaseModel


class City(BaseModel):
    name: str
    latitude: float
    longitude: float

    def get(self):
        return self.longitude, self.latitude, self.name


class CityDist(BaseModel):
    city1: str
    city2: str
    dist: float
    unit: str
