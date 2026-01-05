from pydantic import BaseModel, EmailStr, Field, HttpUrl
from datetime import datetime, date, time
from typing import List, Optional
from enum import Enum

# --- Shared Enums ---
class EventMode(str, Enum):
    online = "online"
    offline = "offline"
    hybrid = "hybrid"



# --- Event Schemas ---
class EventBase(BaseModel):
    slug: str
    title: str
    image: str
    location: str
    venue: str
    date: date
    time: time
    mode: EventMode
    audience: str
    overview: str
    description: str
    organizer: str
    tags: List[str]
    agenda: List[str]

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    booked_spots: int = Field(alias="bookedSpots", default=0)

    class Config:
        from_attributes = True
        populate_by_name = True

# --- User Schemas ---
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str  # Plain text here; hash it in your logic before saving to DB

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True

# --- Booking Schemas ---
class BookingBase(BaseModel):
    event_slug: str = Field(alias="eventSlug")
    event_title: str = Field(alias="eventTitle")
    event_date: date = Field(alias="eventDate")
    event_time: time = Field(alias="eventTime")
    event_location: str = Field(alias="eventLocation")
    user_name: str = Field(alias="userName")
    user_email: EmailStr = Field(alias="userEmail")

class BookingCreate(BookingBase):
    user_id: int = Field(alias="userId")

class BookingResponse(BookingBase):
    id: int
    user_id: int = Field(alias="userId")
    booking_date: datetime = Field(default_factory=datetime.now, alias="bookingDate")

    class Config:
        from_attributes = True
        populate_by_name = True