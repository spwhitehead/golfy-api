import uuid

from fastapi import FastAPI

from models.course import Course
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
async def update_player(player_id):
    pass


@app.delete("/player/{player_id}")
async def delete_player(player_id):
    pass


@app.get("/courses")
async def list_courses():
    return courses.values()


@app.post("/courses")
async def add_course():
    pass


@app.put("/course/{course_id}")
async def update_course(course_id):
    pass


@app.delete("course/{course_id}")
async def delete_course(course_id):
    pass
