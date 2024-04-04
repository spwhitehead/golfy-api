import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}
