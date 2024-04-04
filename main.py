import uuid

from fastapi import FastAPI, HTTPException

from models.course import Course, CreateCourseRequest
from models.player import Player, CreatePlayerRequest


app = FastAPI()

players: dict[uuid.UUID, Player] = {}
courses: dict[uuid.UUID, Course] = {}


@app.get("/players")
async def list_players() -> list[Player]:
    return players.values()


@app.post("/players")
async def add_player(player_detail: CreatePlayerRequest) -> uuid.UUID:
    player_id = uuid.uuid4()
    player = Player(id=player_id,
                    name=player_detail.name,
                    handicap=player_detail.handicap
                    )
    players[player.id] = player
    return player_id


@app.put("/player/{player_id}")
async def update_player(player_id: uuid.UUID, player_detail: CreatePlayerRequest):
    if player_id not in players:
        raise HTTPException(status_code=404, detail="Player not found")

    player = players[player_id]
    player.name = player_detail.name
    player.handicap = player_detail.handicap
    return ("Player updated successfully")


@app.delete("/player/{player_id}")
async def delete_player(player_id: uuid.UUID):
    if player_id not in players:
        raise HTTPException(status_code=404, detail="Player not found")

    players.pop(player_id)
    return ("Player deleted successfully")

# Courses


@app.get("/courses")
async def list_courses() -> list[Course]:
    return courses.values()


@app.post("/courses")
async def add_course(course_detail: CreateCourseRequest) -> uuid.UUID:
    course_id = uuid.uuid4()
    course = Course(id=course_id,
                    name=course_detail.name,
                    location=course_detail.location,
                    num_holes=course_detail.num_holes
                    )
    courses[course.id] = course
    return course_id


@app.put("/course/{course_id}")
async def update_course(course_id):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")


@app.delete("course/{course_id}")
async def delete_course(course_id):
    pass
