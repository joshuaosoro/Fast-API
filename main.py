from fastapi import FastAPI
from api import users, sections, courses


app = FastAPI(
    title="Fast API",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "joshua osoro",
        "email": "joshuaosoro@gmail.com"
    }
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)