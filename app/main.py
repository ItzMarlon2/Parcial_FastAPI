from fastapi import FastAPI
from app.routes import client_routes, reservation_routes
from app.config.config import init_db

app = FastAPI() # type: ignore

app.include_router(client_routes.router
                   , prefix='/clients',
                   tags=["Clients"])

app.include_router(reservation_routes.router
                   , prefix='/reservations',
                   tags=["Reservations"])

@app.get("/")
async def root():
    return {"Parcial 1: Marlon Campo - 240220231004"}

init_db()