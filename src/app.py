from fastapi import FastAPI

from user.infrastructure.controllers.user_controller import user_router

app = FastAPI()

app.include_router(user_router)

@app.get('/')
def read_root():
    return {"Welcome": "Welcome to my api"}
