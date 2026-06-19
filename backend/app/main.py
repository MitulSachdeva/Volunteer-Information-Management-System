from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import (
    volunteers,
    auth_routes,
    admin
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Volunteer Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    volunteers.router
)

app.include_router(
    auth_routes.router
)

app.include_router(
    admin.router
)