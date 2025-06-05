from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# Conexión a MongoDB
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://admin:password@mongodb:27017")
    app.mongodb = app.mongodb_client["larrain_db"]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
async def root():
    return {"message": "API de Importadora Larraín"}

@app.get("/productos")
async def listar_productos():
    productos = await app.mongodb["productos"].find().to_list(100)
    return productos