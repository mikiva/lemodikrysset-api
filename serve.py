from uvicorn import run


if __name__ == "__main__":
    run("main:app", port=3001,  reload=True, log_level="debug")