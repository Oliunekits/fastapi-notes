from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteUpdate


class NotesRepository:

    @staticmethod
    def get_all(db: Session, query: Optional[str] = None, tag: Optional[str] = None) -> List[Note]:
        q = db.query(Note)
        if query:
            q = q.filter(
                or_(
                    Note.title.ilike(f"%{query}%"),
                    Note.content.ilike(f"%{query}%"),
                )
            )
        if tag:
            q = q.filter(Note.tags.ilike(f"%{tag}%"))
        return q.order_by(Note.created_at.desc()).all()

    @staticmethod
    def get_by_id(db: Session, note_id: int) -> Optional[Note]:
        return db.query(Note).filter(Note.id == note_id).first()

    @staticmethod
    def create(db: Session, note_in: NoteCreate) -> Note:
        db_note = Note(
            title=note_in.title,
            content=note_in.content,
            tags=note_in.tags,  # тут вже рядок
        )
        db.add(db_note)
        db.commit()
        db.refresh(db_note)
        return db_note

    @staticmethod
    def update(db: Session, note_id: int, note_in: NoteUpdate) -> Optional[Note]:
        db_note = db.query(Note).filter(Note.id == note_id).first()
        if not db_note:
            return None
        db_note.title = note_in.title
        db_note.content = note_in.content
        db_note.tags = note_in.tags
        db.commit()
        db.refresh(db_note)
        return db_note

    @staticmethod
    def delete(db: Session, note_id: int) -> bool:
        db_note = db.query(Note).filter(Note.id == note_id).first()
        if not db_note:
            return False
        db.delete(db_note)
        db.commit()
        return True
