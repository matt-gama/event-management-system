from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import * 
from app.core.security import verify_bearer_token
from app.crud.crud_user import create_user, delete_user
from app.core.database import get_db



router = APIRouter()

@router.post('/register')
async def register(
    payload: Register,
    db: AsyncSession = Depends(get_db),
    token: str = Depends(verify_bearer_token)
):
    try:
        await create_user(db, name=payload.name, lastname=payload.lastname, email=payload.email, password=payload.password)
        return {"message": "User registered successfully"}

    except HTTPException as ex:
        print(f"HTTP Error in register: {ex.detail}")
        raise ex  # re-levanta para FastAPI retornar status correto

    except Exception as ex:
        print(f"Unexpected error in register: {ex}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
    
@router.post('/delete/{id_user}')
async def delete(
    id_user: int,
    db: AsyncSession = Depends(get_db),
    token: str = Depends(verify_bearer_token)
):
    try:
        await delete_user(db, id_user)
        return {"message": "User deleted successfully"}

    except HTTPException as ex:
        print(f"HTTP Error in register: {ex.detail}")
        raise ex  # re-levanta para FastAPI retornar status correto

    except Exception as ex:
        print(f"Unexpected error in register: {ex}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )