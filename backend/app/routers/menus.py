from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db import get_session
from ..models import Menu
from ..deps import get_current_superuser

router = APIRouter()

@router.get("/")
def list_menus(session: Session = Depends(get_session), current=Depends(get_current_superuser)):
    return session.exec(select(Menu)).all()

@router.post("/")
def create_menu(m: Menu, session: Session = Depends(get_session), current=Depends(get_current_superuser)):
    session.add(m)
    session.commit()
    session.refresh(m)
    return m
