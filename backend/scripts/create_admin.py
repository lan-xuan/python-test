#!/usr/bin/env python3
"""
Create admin user script.
Usage: python backend/scripts/create_admin.py [username] [password]
"""
import sys
from sqlmodel import Session, select
from app.db import engine
from app.models import User
from app.security import get_password_hash

def create_admin(username: str, password: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        user = session.exec(statement).first()
        if user:
            print(f"User '{username}' already exists (id={{user.id}}).\n")
            return
        hashed = get_password_hash(password)
        admin = User(username=username, hashed_password=hashed, is_superuser=True, is_active=True)
        session.add(admin)
        session.commit()
        session.refresh(admin)
        print(f"Created admin '{username}' with id {{admin.id}}.\n")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        u = sys.argv[1]
        p = sys.argv[2]
    else:
        u = "admin"
        p = "Admin123"
    create_admin(u,p)