from pydantic import BaseModel, Field

class Property(BaseModel):
    id: str = Field(None, alias="_id")
    property_id: int
    property_name: str
    address: str
    city: str
    state: str
