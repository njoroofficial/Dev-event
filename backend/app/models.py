from pydantic import BaseModel

class Event(BaseModel):
    id : int 
    slug: str
    title: str
    image: str
    location: str
    venue: str
    date: str
    time: str
    mode: str
    audience: str
    overview: str
    description: str
    organizer: str
    tags: str
    agenda: str
    bookedSpots: int
