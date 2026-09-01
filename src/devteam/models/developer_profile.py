from pydantic import BaseModel


class DeveloperProfile(BaseModel):
    id:str
    name:str
    skills:list[str]