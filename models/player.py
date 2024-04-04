from uuid import UUID
from pydantic import BaseModel

# Player:
# ID
# Name
# Handicap


class Player(BaseModel):
    id: UUID
    name: str
    handicap: float


class CreatePlayerRequest(BaseModel):
    name: str
    handicap: float
