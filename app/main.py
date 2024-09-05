from fastapi import FastAPI
from app.routes import client_routes

app = FastAPI() # type: ignore

app.include_router(client_routes.router
                   , prefix='/clients',
                   tags=["Clients"])

@app.get("/")
async def root():
    return {"Parcial 1: Marlon Campo - 240220231004"}