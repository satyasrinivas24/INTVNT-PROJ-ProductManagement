import logging
from fastapi import APIRouter, HTTPException, Depends
from config.db_utils import get_db
from models.index import users
from schemas.index import User
from sqlalchemy import select, update, insert, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user = APIRouter()


@user.get('/')
async def read_data(db: Session = Depends(get_db)):
    try:
        stmt = select(users)
        logger.info(f"Executing statement: {stmt}")
        result = db.execute(stmt).mappings().all()
        logger.info(f"Fetched data: {result}")
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Database error")


@user.get('/{id}')
async def read_single_data(id: int, db: Session = Depends(get_db)):
    try:
        stmt = select(users).where(users.c.id == id)
        result = db.execute(stmt).mappings().all()
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error fetching user with id {id}: {e}")
        raise HTTPException(status_code=500, detail="Database error")


@user.post('/')
async def write_data(user: User, db: Session = Depends(get_db)):
    try:
        stmt = insert(users).values(
            name=user.name,
            email=user.email,
            password=user.password
        )
        db.execute(stmt)
        db.commit()
        result = db.execute(select(users)).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error inserting user: {e}")
        raise HTTPException(status_code=500, detail="Database error")


@user.put('/{id}')
async def update_data(id: int, user: User, db: Session = Depends(get_db)):
    try:
        stmt = update(users).where(users.c.id == id).values(
            name=user.name,
            email=user.email,
            password=user.password
        )
        db.execute(stmt)
        db.commit()
        result = db.execute(select(users).where(users.c.id == id)).mappings().all()
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error updating user with id {id}: {e}")
        raise HTTPException(status_code=500, detail="Database error")


@user.delete('/{id}')
async def delete_data(id: int, db: Session = Depends(get_db)):
    try:
        stmt = delete(users).where(users.c.id == id)
        db.execute(stmt)
        db.commit()
        result = db.execute(select(users)).mappings().all()
        return result
    except SQLAlchemyError as e:
        logger.error(f"Error deleting user with id {id}: {e}")
        raise HTTPException(status_code=500, detail="Database error")