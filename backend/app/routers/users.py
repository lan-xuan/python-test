from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from ..db import get_session
from ..crud import create_user, get_user_by_username
from ..deps import get_current_superuser
from ..models import User

router = APIRouter()

@router.get("/", response_model=list[User])
def list_users(session: Session = Depends(get_session), current=Depends(get_current_superuser)):
    return session.exec(select(User)).all()

@router.post("/", response_model=User)
def create_new_user(u: User, session: Session = Depends(get_session), current=Depends(get_current_superuser)):
    if get_user_by_username(session, u.username):
        raise HTTPException(status_code=400, detail="User exists")
    return create_user(session, u.username, u.hashed_password, is_superuser=u.is_superuser, full_name=u.full_name)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, session: Session = Depends(get_session), current=Depends(get_current_superuser)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(user)
    session.commit()
