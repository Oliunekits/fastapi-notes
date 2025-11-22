from pydantic import BaseModel
from typing import Optional


class NoteBase(BaseModel):
    title: str
    content: str
    # теги зберігаємо як один рядок: "study,python"
    tags: Optional[str] = None


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    pass


class NoteOut(NoteBase):
    id: int

    class Config:
        from_attributes = True  # для роботи з ORM-моделями
