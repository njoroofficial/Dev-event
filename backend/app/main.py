from fastapi import FastAPI
from models import Event

# initializing the app
app = FastAPI()

# health check route
@app.get("/")
def health_check():
    return {"status":"online", "message":"The Dev-Event application is running"}

# example event

events = [Event(
    title = "React Conference 2026",
    image = "/images/event1.png",
    location = "San Francisco, CA",
    venue = "Tech Convention Center",
    date = "2025-12-12",
    time = "09:00",
    mode = "hybrid",
    audience = "React Developers, Frontend Engineers, Full-stack Developers",
    overview = "Join the biggest React event of the year! Learn about the latest React features, best practices, and network with industry leaders. This conference features keynote speakers from Meta, Vercel, and other major tech companies. Topics include React Server Components, Suspense, concurrent rendering, and the future of React development. Whether you're a beginner or an expert, there's something for everyone.",
    description = "Annual React conference bringing together developers from around the world to learn about the latest in React development",
    organizer = "React Community Team",
    tags = "react",
    slug = "react-conf-2026",
    agenda = "Registration & Welcome Coffee (8:00 AM)",
    id = 1,
    bookedSpots= 10
    ),
    Event(
    title = "React Conference 2026",
    image = "/images/event1.png",
    location = "San Francisco, CA",
    venue = "Tech Convention Center",
    date = "2025-12-12",
    time = "09:00",
    mode = "hybrid",
    audience = "React Developers, Frontend Engineers, Full-stack Developers",
    overview = "Join the biggest React event of the year! Learn about the latest React features, best practices, and network with industry leaders. This conference features keynote speakers from Meta, Vercel, and other major tech companies. Topics include React Server Components, Suspense, concurrent rendering, and the future of React development. Whether you're a beginner or an expert, there's something for everyone.",
    description = "Annual React conference bringing together developers from around the world to learn about the latest in React development",
    organizer = "React Community Team",
    tags = "react",
    slug = "react-conf-2026",
    agenda = "Registration & Welcome Coffee (8:00 AM)",
    id = 2,
    bookedSpots= 30
    )]

# get all events
@app.get("/events")
def get_all_events():
    return events

# get one event
@app.get("/event/{id}")
def get_one_event(id: int):
    for event in events:
        if event.id == id:
            return event
    
    return "Event not found"

# add an event
@app.post("/event")
def add_event(event: Event):
    events.append(event)
    return event

# update a event
@app.put("/event")
def update_event(id: int, event: Event):
    for i in range(len(events)):
        if events[i].id == id:
            events[i] = event
            return "Event updated successfully"

    return "Event not found" 

# delete an event
@app.delete("/event")
def del_event(id: int):
    for i in range(len(events)):
        if events[i].id == id:
            del events[id]
            return "Event deleted successfully"
        
    return "Event not found"
