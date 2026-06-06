
from datetime import datetime, timezone
from uuid import uuid4
from typing import Optional , List

from sqlmodel import Field , SQLModel , Relationship

def _uuid() -> str:
    return str(uuid4())

def _now() -> datetime:
    return datetime.now(timezone.utc)

class Thumbnail(SQLModel , table=True):
    id: str = Field(default_factory=_uuid , primary_key = True)
    job_id: str = Field(foreign_key = "job.id")
    style_name:str = Field(default="")
    status:str = Field(default="Pending")
    error_message:Optional[str] = Field(default=None)
    created_at:datetime = Field(default_factory=_now)

    job : Optional["Job"] = Relationship(back_populates="thumbnails")

class Job(SQLModel , table=True):
    id : str = Field(default_factory=_uuid, primary_key=True)
    prompt:str = Field(default="")
    num_thumbnail:int = Field(default = 1 , ge=1, le=2)
    headshot_url: str = Field(default = "")
    status : str = Field(default = "Pending")
    created_at : datetime = Field(default_factory=_now)

    thumbnails:List[Thumbnail] = Relationship(back_populates= "job")