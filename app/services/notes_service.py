from typing import List, Optional
from sqlalchemy.orm import Session
from app.repositories.notes_repository import NotesRepository
from app.schemas.note import NoteCreate, NoteUpdate
from app.models.note import Note


class NotesService:

    @staticmethod
    def list_notes(db: Session, query: Optional[str] = None, tag: Optional[str] = None) -> List[Note]:
        return NotesRepository.get_all(db, query=query, tag=tag)

    @staticmethod
    def get_note(db: Session, note_id: int) -> Optional[Note]:
        return NotesRepository.get_by_id(db, note_id)

    @staticmethod
    def create_note(db: Session, note_in: NoteCreate) -> Note:
        return NotesRepository.create(db, note_in)

    @staticmethod
    def update_note(db: Session, note_id: int, note_in: NoteUpdate) -> Optional[Note]:
        return NotesRepository.update(db, note_id, note_in)

    @staticmethod
    def delete_note(db: Session, note_id: int) -> bool:
        return NotesRepository.delete(db, note_id)
