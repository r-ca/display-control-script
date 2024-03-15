from pydantic import BaseModel


class DisplayRequest(BaseModel):
    state: bool
