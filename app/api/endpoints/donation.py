from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud import donation_crud
from app.models import User
from app.schemas import DonationDB, DonationCreate, UserDonationDB
from app.services.investment import check_for_avalaible_projects

router = APIRouter()


@router.post(
        '/',
        response_model=UserDonationDB,
        response_model_exclude_none=True,
    )
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):

    donation, projects = await check_for_avalaible_projects(donation, session)

    if projects:
        session.add_all(projects)

    new_donation = await donation_crud.create(
        donation, session, user
    )

    return new_donation


@router.get(
        '/',
        response_model=list[DonationDB],
        dependencies=[Depends(current_superuser)],
        response_model_exclude_none=True,
)
async def get_all_donatations(
        session: AsyncSession = Depends(get_async_session),
):
    all_donations = await donation_crud.get_list(
        session=session,
    )
    return all_donations


@router.get('/my',
            response_model=list[UserDonationDB],
            dependencies=[Depends(current_user)])
async def get_user_donatations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    user_donations = await donation_crud.get_by_user(
        session=session, user=user,
    )
    return user_donations
