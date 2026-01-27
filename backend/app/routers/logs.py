from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from ..db import get_session
from ..models import Log
from ..deps import get_current_superuser

router = APIRouter()

@router.get("/")
def list_logs(session: Session = Depends(get_session), current=Depends(get_current_superuser)):
    return session.exec(select(Log).order_by(Log.created_at.desc())).all()
