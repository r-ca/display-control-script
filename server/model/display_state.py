from pydantic import BaseModel


class DisplayState(BaseModel):
    hostname: str
    state: bool
