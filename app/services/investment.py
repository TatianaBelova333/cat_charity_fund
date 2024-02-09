from datetime import datetime

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas import CharityPrjectCreate, ProjectInvestement, DonationCreate, DonationCreateFull
from app.crud import charity_project_crud, donation_crud


async def check_for_avalaible_investments(
        charity_project: CharityPrjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    available_investments = await donation_crud.get_not_fullyinvested_objs(
        session=session,
    )

    charity_project = ProjectInvestement(**charity_project.dict())

    invt_for_update = []

    for invt in available_investments:
        if charity_project.fully_invested:
            break

        required_amount = charity_project.full_amount - charity_project.invested_amount

        invt_avail_amt = invt.full_amount - invt.invested_amount

        if invt_avail_amt >= required_amount:
            await close_investment_item(charity_project)
            if invt_avail_amt == required_amount:
                await close_investment_item(invt)
            else:
                invt.invested_amount += required_amount
        else:
            await close_investment_item(invt)
            charity_project.invested_amount += invt_avail_amt

        invt_for_update.append(invt)
    return charity_project, invt_for_update


async def close_investment_item(item):
    item.invested_amount = item.full_amount
    item.fully_invested = True
    item.close_date = datetime.now()
    return item


async def check_for_avalaible_projects(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
):
    available_projects = await charity_project_crud.get_not_fullyinvested_objs(
        session=session,
    )
    donation = DonationCreateFull(**donation.dict())
    projects_for_update = []

    for project in available_projects:
        if donation.fully_invested:
            break

        left_amount = donation.full_amount - donation.invested_amount

        project_rqd_amnt = project.full_amount - project.invested_amount

        if project_rqd_amnt >= left_amount:
            await close_investment_item(donation)
            if project_rqd_amnt == left_amount:
                await close_investment_item(project)
            else:
                project.invested_amount += left_amount
        else:
            await close_investment_item(project)
            donation.invested_amount += project_rqd_amnt

        projects_for_update.append(project)

    return donation, projects_for_update
