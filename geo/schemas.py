from pydantic import BaseModel


class City(BaseModel):
    name: str
    latitude: float
    longitude: float

    def get(self):
        return self.longitude, self.latitude, self.name


class Coordinates(BaseModel):
    latitude: float
    longitude: float
