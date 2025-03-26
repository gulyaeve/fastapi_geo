from uvicorn import run


def main():
    print("Hello from fastapi-geo!")
    run(app="app:app", reload=True)


if __name__ == "__main__":
    main()
