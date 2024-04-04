from pydantic import BaseModel


# Course:
# Name
# Location
# num holes

class Course(BaseModel):
    name: str
    location: str
    num_holes: int
