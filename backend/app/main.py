from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db import engine
from . import models
from .routers import auth, users, menus, logs, dbadmin

models.SQLModel.metadata.create_all(engine)

app = FastAPI(title="Admin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth")
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(menus.router, prefix="/api/menus", tags=["menus"])
app.include_router(logs.router, prefix="/api/logs", tags=["logs"])
app.include_router(dbadmin.router, prefix="/api/db", tags=["db"])

@app.get("/health")
def health():
    return {"status": "ok"}