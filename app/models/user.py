from typing import List
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    donations: Mapped[List['Donation']] = relationship(
        'Donation',
        back_populates='user',
        lazy='selectin',
    )
