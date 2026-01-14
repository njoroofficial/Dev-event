from fastapi import Depends,FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import EventBase
from database import SessionLocal, engine
import database_model
from sqlalchemy.orm import Session
import auth

# initializing the app
app = FastAPI()
app.include_router(auth.router)

# setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create database tables
database_model.Base.metadata.create_all(bind=engine)

# health check route
@app.get("/")
def health_check():
    return {"status":"online", "message":"The Dev-Event application is running"}

# example event

events = [EventBase(
    title = "React Conference 2026",
    image = "/images/event1.png",
    location = "San Francisco, CA",
    venue = "Tech Convention Center",
    date = "2026-12-12",
    time = "09:00",
    mode = "hybrid",
    audience = "React Developers, Frontend Engineers, Full-stack Developers",
    overview = "Join the biggest React event of the year! Learn about the latest React features, best practices, and network with industry leaders. This conference features keynote speakers from Meta, Vercel, and other major tech companies. Topics include React Server Components, Suspense, concurrent rendering, and the future of React development. Whether you're a beginner or an expert, there's something for everyone.",
    description = "Annual React conference bringing together developers from around the world to learn about the latest in React development",
    organizer = "React Community Team",
    tags = [
        "react",
        "javascript",
        "frontend",
        "conference"
      ],
    slug = "react-conf-2026",
    agenda = [
        "Registration & Welcome Coffee (8:00 AM)",
        "Opening Keynote: Future of React (9:00 AM)",
        "Workshop: Server Components Deep Dive (10:30 AM)",
        "Lunch Break & Networking (12:30 PM)",
        "Panel Discussion: React Ecosystem (2:00 PM)",
        "Advanced Performance Optimization (3:30 PM)",
        "Closing Remarks & Announcements (5:00 PM)"
      ],
    id = 1,
    ),
    EventBase(
    title = "Next.js 16 Workshop",
    image = "/images/event2.png",
    location = "Virtual Event",
    venue = "Online via Zoom",
    date = "2026-11-20",
    time = "11:00",
    mode = "online",
    audience = "Web Developers, React Developers, Full-stack Engineers",
    overview = "Join the biggest React event of the year! Learn about the latest React features, best practices, and network with industry leaders. This conference features keynote speakers from Meta, Vercel, and other major tech companies. Topics include React Server Components, Suspense, concurrent rendering, and the future of React development. Whether you're a beginner or an expert, there's something for everyone.",
    description = "Annual React conference bringing together developers from around the world to learn about the latest in React development",
    organizer = "Vercel",
    tags = [
        "nextjs",
        "react",
        "fullstack",
        "workshop",
        "vercel"
      ],
    slug = "nextjs-16-workshop",
    agenda = [
        "Introduction to Next.js 15 Features",
        "App Router Architecture",
        "Server Components vs Client Components",
        "Server Actions and Form Handling",
        "Data Fetching Patterns",
        "Caching Strategies",
        "Deployment Best Practices",
        "Q&A Session"
      ],
    id = 2,
    )]

def get_db():
    # open database
    db = SessionLocal()
    try:
    # use database
        yield db
    # close database
    finally:
        db.close()

def init_db():
    db = SessionLocal()

    count = db.query(database_model.Event).count()

    if count == 0:
        for event in events:
            db.add(database_model.Event(**event.model_dump()))
    db.commit()

init_db()

# get all events
@app.get("/events")
def get_all_events(db: Session = Depends(get_db)): # dependency injection

    # fetch all events from database
    db_events = db.query(database_model.Event).all()
    return db_events

# get one event
@app.get("/events/{slug}")
def get_one_event(slug: str, db: Session = Depends(get_db)):
    db_event = db.query(database_model.Event).filter(database_model.Event.slug == slug).first()
    
    if db_event: 
        return db_event
    
    return "Event not found"

# add an event
@app.post("/events")
def add_event(event: EventBase, db: Session = Depends(get_db)):

    # add events to database
    db.add(database_model.Event(**event.model_dump()))
    db.commit()
    return event

# update a event
@app.put("/events/{slug}")
def update_event(slug: str, event: EventBase, db: Session = Depends(get_db)):
    # check if event exits
    db_event = db.query(database_model.Event).filter(database_model.Event.slug == slug).first()

    if db_event:
        db_event.title = event.title
        db_event.image = event.image
        db_event.location = event.location
        db_event.venue = event.venue
        db_event.date = event.date
        db_event.time = event.time
        db_event.mode = event.mode
        db_event.audience = event.audience
        db_event.agenda = event.agenda
        db_event.overview = event.overview
        db_event.description = event.description
        db_event.tags = event.tags
        db_event.slug = event.slug
        db_event.organizer = event.organizer

        db.commit()
        return "Event updated"
    else:
        return "Event not found" 
 
# delete an event
@app.delete("/events/{slug}")
def del_event(slug: str, db: Session = Depends(get_db)):
    db_event = db.query(database_model.Event).filter(database_model.Event.slug == slug).first()

    if db_event:
        db.delete(db_event)
        db.commit()
    else:
        return "Event not found"
