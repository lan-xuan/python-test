from sqlmodel import Session, select
from .models import User
from .security import get_password_hash

def get_user_by_username(session: Session, username: str):
    return session.exec(select(User).where(User.username == username)).first()


def create_user(session: Session, username: str, password: str, is_superuser: bool = False, full_name: str | None = None):
    hashed = get_password_hash(password)
    user = User(username=username, hashed_password=hashed, is_superuser=is_superuser, full_name=full_name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
