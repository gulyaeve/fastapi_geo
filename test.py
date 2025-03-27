from config import cache


code = '''
return redis.call('set', KEYS[1], ARGV[1])
'''


if __name__ == "__main__":
    # cities = cache.georadius("cities", 0, 0, 22000, "km")
    # print(cities)
    cache.eval(code, 1, "mykey", "Hello from lua")