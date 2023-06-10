from uvicorn import run


if __name__ == "__main__":
    run("main:app", port=3001, host="0.0.0.0",  reload=True, log_level="debug")