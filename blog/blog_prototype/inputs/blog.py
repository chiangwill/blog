from typing import Optional

from pydantic import BaseModel, Field, validator


class PostCreateInput(BaseModel):

    user_id: int
    title: str = Field(..., max_length=255, blank=False)
    description: Optional[str] = None


class PostUpdateInpute(BaseModel):

    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None


class CommentCreateInput(BaseModel):

    user_id: int
    post_id: int
    description: Optional[str] = None


class CommentUpdateInpute(BaseModel):

    description: Optional[str] = None
