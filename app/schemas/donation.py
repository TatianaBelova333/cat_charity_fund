from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: Optional[int] = Field(gt=0)
    create_date: Optional[datetime]


class UserDonationDB(DonationBase):
    id: int

    class Config:
        orm_mode = True


class DonationDB(DonationBase):
    id: int
    invested_amount: int = 0
    fully_invested: bool = False
    close_date: Optional[datetime]
    user_id: int

    class Config:
        orm_mode = True


class DonationCreate(BaseModel):
    comment: Optional[str]
    full_amount: int = Field(gt=0)

    class Config:
        extra = Extra.forbid


class DonationCreateFull(BaseModel):
    comment: Optional[str]
    full_amount: int = Field(gt=0)
    invested_amount: int = 0
    fully_invested: bool = False
    create_date: Optional[datetime]
    close_date: Optional[datetime] = None
