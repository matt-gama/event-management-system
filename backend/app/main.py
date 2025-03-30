from fastapi import FastAPI
from app.core.database import init_db
from app.routes.users import router as users


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()  # Cria as tabelas automaticamente

@app.get('/')
async def main():
    return {"message": "Welcome the Event Menagement System", "version": ""}

app.include_router(router=users, prefix='/api/v1/user')