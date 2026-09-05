from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    text: str = Field(min_length=1)


class NoteUpdate(BaseModel):
    text: str = Field(min_length=1)


class Note(BaseModel):
    id: int
    text: str
