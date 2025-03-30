from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.models.user import * 



async def create_user(db: AsyncSession, name: str, lastname: str, email: str, password: str):
    try:

        new_user = User(name=name, lastname=lastname, email=email, password=password)

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)

    except IntegrityError as e:
        await db.rollback()
        # Verifica se o erro é por chave duplicada
        if 'duplicar valor da chave viola a restrição de unicidade "users_email_key"' in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered."
            )
        # Outros erros de integridade
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database integrity error."
        )
    
    except Exception as ex:
        await db.rollback()
        print(f"Unexpected error: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error occurred"
        )

async def delete_user(db: AsyncSession, id_user:int):
    try:

        stmt = delete(User).where(User.id == id_user)
        result = await db.execute(stmt)
        await db.commit()

        if result.rowcount == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

    except IntegrityError as e:
        await db.rollback()
        # Verifica se o erro é por chave duplicada
        if 'duplicar valor da chave viola a restrição de unicidade "users_email_key"' in str(e.orig):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered."
            )
        # Outros erros de integridade
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database integrity error."
        )
    
    except Exception as ex:
        await db.rollback()
        print(f"Unexpected error: {ex}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error occurred"
        )
