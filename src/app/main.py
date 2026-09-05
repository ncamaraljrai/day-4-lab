from fastapi import FastAPI, HTTPException, status

from app.models import Note, NoteCreate, NoteUpdate
from app.store import store

app = FastAPI(title="WIP=1 Notes API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/notes", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate) -> Note:
    return store.create(payload.text)


@app.get("/notes/{note_id}", response_model=Note)
def read_note(note_id: int) -> Note:
    note = store.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@app.get("/notes", response_model=list[Note])
def list_notes() -> list[Note]:
    return store.list_all()


@app.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, payload: NoteUpdate) -> Note:
    note = store.update(note_id, payload.text)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int) -> None:
    if not store.delete(note_id):
        raise HTTPException(status_code=404, detail="note not found")
