from fastapi import FastAPI

from src import endpoints
from src.containers import Container

from bootstrap import *


def server() -> FastAPI:
    container = Container()
    
    app = FastAPI(
        title="Articles API",
        description="Working with dependency injector"
    )    
    app.container = container
    app.include_router(endpoints.router)

    return app

app = server()

@app.get("/", tags=["Start"])
def main():
    return {"msg": "Working with dependency injection"}
