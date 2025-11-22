from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.note import NoteCreate, NoteUpdate, NoteOut
from app.services.notes_service import NotesService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[NoteOut])
def list_notes(
    q: Optional[str] = Query(default=None, description="Search in title or content"),
    tag: Optional[str] = Query(default=None, description="Filter by tag"),
    db: Session = Depends(get_db),
):
    return NotesService.list_notes(db, query=q, tag=tag)


@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = NotesService.get_note(db, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.post("/", response_model=NoteOut)
def create_note(note_in: NoteCreate, db: Session = Depends(get_db)):
    return NotesService.create_note(db, note_in)


@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_in: NoteUpdate, db: Session = Depends(get_db)):
    note = NotesService.update_note(db, note_id, note_in)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.delete("/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    ok = NotesService.delete_note(db, note_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Deleted"}
