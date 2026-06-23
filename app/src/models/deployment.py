from pydantic import BaseModel

class Deployment(BaseModel):
    id:int
    application:str
    version:str
    status:str