from pydantic import BaseModel

class Application(BaseModel):
    id:int
    name:str
    environment:str
    status:str
    