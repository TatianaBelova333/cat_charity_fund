from typing import Optional

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def check_name_duplicates(
            self,
            project_name: Optional[str],
            session: AsyncSession,
    ) -> Optional[int]:
        """
        Return True if the project name (case-insensitive) is already in db.
        False, otherwise.

        """
        project_name = project_name.lower() if project_name else project_name

        exists_criteria = (
            select(CharityProject).where(
                func.lower(CharityProject.name) == project_name
            ).exists()
        )

        duplicate_name_exists = await session.scalar(
            select(True).where(exists_criteria)
        )

        return bool(duplicate_name_exists)

    async def remove(
            self,
            db_obj: CharityProject,
            session: AsyncSession,
    ):
        """
        Remove the db_obj from db.

        """
        await session.delete(db_obj)
        await session.commit()
        return db_obj


charity_project_crud = CRUDCharityProject(CharityProject)
