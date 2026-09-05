from app.models import Note


class NoteStore:
    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._next_id = 1

    def reset(self) -> None:
        self._notes.clear()
        self._next_id = 1

    def create(self, text: str) -> Note:
        note = Note(id=self._next_id, text=text.strip())
        self._notes[note.id] = note
        self._next_id += 1
        return note

    def get(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)

    def list_all(self) -> list[Note]:
        return list(self._notes.values())

    def update(self, note_id: int, text: str) -> Note | None:
        if note_id not in self._notes:
            return None
        note = Note(id=note_id, text=text.strip())
        self._notes[note_id] = note
        return note

    def delete(self, note_id: int) -> bool:
        return self._notes.pop(note_id, None) is not None


store = NoteStore()
