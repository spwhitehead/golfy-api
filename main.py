import uuid

from fastapi import FastAPI

from models.course import Course
from models.player import Player


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}


@app.get("/courses")
async def list_courses():
    pass


@app.post("/courses")
async def add_course():
    pass


@app.put("/course/{course_id}")
async def update_course(course_id):
    pass


@app.delete("course/{course_id}")
async def delete_course(course_id):
    pass


@app.get("/players")
async def list_players():
    pass


@app.post("/players")
async def add_player():
    pass


@app.put("/player/{player_id}")
async def update_player(player_id):
    pass


@app.delete("/player/{player_id}")
async def delete_player(player_id):
    pass
