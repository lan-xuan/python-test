from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .db import init_db
from .routers import auth, users, menus, logs, dbadmin

app = FastAPI(title="Admin API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(menus.router, prefix="/api/menus", tags=["menus"])
app.include_router(logs.router, prefix="/api/logs", tags=["logs"])
app.include_router(dbadmin.router, prefix="/api/db", tags=["db"])

@app.get("/health")
def health():
    return {"status": "ok"}
