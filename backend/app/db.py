from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://admin:password@mongodb:27017")
    app.mongodb = app.mongodb_client["larrain_db"]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()