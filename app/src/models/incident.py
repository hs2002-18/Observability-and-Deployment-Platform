from pydantic import BaseModel

class Incident(BaseModel):
    id:int
    service:str
    severity:str
    status:str