from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASS: str

    @property
    def redis_url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    class Config:
        env_file = ".env"


settings = Settings()
