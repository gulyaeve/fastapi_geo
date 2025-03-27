from uvicorn import run


def main():
    print("Hello from fastapi-city!")
    run(app="app:app", reload=True)


if __name__ == "__main__":
    main()
