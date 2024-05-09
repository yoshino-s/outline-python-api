# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .comment import Comment
from .._models import BaseModel

__all__ = ["CommentUpdateResponse"]


class CommentUpdateResponse(BaseModel):
    data: Optional[Comment] = None
