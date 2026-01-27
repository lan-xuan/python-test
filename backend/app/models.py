from typing import Optional
from sqlmodel import SQLModel, Field, Column, String
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(sa_column=Column("username", String(50), unique=True, nullable=False))
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False
    full_name: Optional[str] = None

class Menu(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    path: Optional[str] = None
    parent_id: Optional[int] = None

class Log(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = None
    action: str
    detail: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
