from fastapi import FastAPI, HTTPException
from typing import List
from models import Property
from bson import ObjectId
from fastapi import Path
from database import (
    fetch_all_properties, fetch_property_details, create_new_property,
    update_property_details, find_cities_by_state, find_similar_properties
)

app = FastAPI()

@app.post("/create_new_property/", response_model=dict)
async def create_new_property_endpoint(property: Property):
    try:
        result = create_new_property(property)
        return {"message": "Property created successfully and saved in the database", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_model=List[Property])
async def fetch_all_properties_endpoint():
    try:
        properties = fetch_all_properties()
        if properties:
            return properties
        else:
            raise HTTPException(status_code=404, detail="No properties found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fetch_property_details/", response_model=List[Property])
async def fetch_properties_by_city(city: str):
    try:
        properties = fetch_property_details(city)
        if properties:
            return properties
        else:
            raise HTTPException(status_code=404, detail="Properties not found for the given city")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from bson import ObjectId




@app.put("/update_property_details/{property_id}", response_model=dict)
async def update_properties(property_id: str, property: Property):
    try:
        if not ObjectId.is_valid(property_id):
            raise HTTPException(status_code=400, detail="Invalid property_id format")
        
        result = update_property_details(property_id, property)
        return {"message": "Property details updated successfully", "data": result}
    except Exception as e:
        print("Error:", e)  # Print the error for debugging purposes
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/find_cities_by_state/", response_model=List[str])
async def find_cities(state: str):
    try:
        cities = find_cities_by_state(state)
        if cities:
            return cities
        else:
            raise HTTPException(status_code=404, detail="No cities found for the given state")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/find_similar_properties/", response_model=List[Property])
async def find_similar(property_id: int):
    try:
        properties = find_similar_properties(property_id)
        if properties:
            return properties
        else:
            raise HTTPException(status_code=404, detail="No similar properties found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
