from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import date, datetime
from typing import Optional


class ContactModel(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(max_length=50)
    birthday: date
    additional_info: str = Field(max_length=250)


class ContactResponse(ContactModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birth_date: date
    additional: str
    created_at: datetime | None
    updated_at: Optional[datetime] | None

    model_config = ConfigDict(from_attributes=True)


class ContactUpdate(ContactModel):
    done: bool


class ContactStatusUpdate(BaseModel):
    done: bool
