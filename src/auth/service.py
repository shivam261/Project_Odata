from sqlmodel import Session, select
from .model import User
from fastapi import HTTPException

def authenticate_user(username: str, password: str, session: Session) -> User:
    """
    Returns the User object if credentials are correct,
    otherwise raises HTTPException 401.
    """
    statement = select(User).where(User.username == username)
    user = session.exec(statement).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def register_user(user: User, session: Session) -> User:
    """
    Register a new user.
    Raises HTTPException if username already exists.
    Returns the created User object.
    """
    # Check if user already exists
    statement = select(User).where(User.username == user.username)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Add new user to the database
    session.add(user)
    session.commit()
    session.refresh(user)

    return user