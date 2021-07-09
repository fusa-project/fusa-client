from pydantic import BaseModel, conlist
from typing import Optional

class UserSchema(BaseModel):
    category: str
    username: str

class TagSchema(BaseModel):
    username: str
    source_tags: conlist(str, min_items=1, max_items=10)

class ParentSchema(BaseModel):
    parent_id: int
    parent_chunk: conlist(float, min_items=1, max_items=2)

class AudioSchema(BaseModel):
    name: str
    format: str
    size: float
    duration: float
    recorded_at: int
    uploaded_at: int
    latitude: float
    longitude: float
    data: str
    user: UserSchema
    tags: Optional[conlist(TagSchema, min_items=1, max_items=None)]
    has_parent: bool
    parent: Optional[ParentSchema]