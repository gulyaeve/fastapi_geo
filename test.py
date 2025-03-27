from config import cache


if __name__ == "__main__":
    cities = cache.georadius("cities", 0, 0, 22000, "km")
    print(cities)