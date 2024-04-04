from uuid import UUID
from pydantic import BaseModel


# Course:
# Name
# Location
# num holes

class Course(BaseModel):
    id: UUID
    name: str
    location: str
    num_holes: int
