# FASTAPI web framework Server for CityScape porject Inviz Labs


This FAST API server provides endpoints to retrieve properties information, with support for adding new branches. It uses Mongo db as the database backend. AND CURD

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhi19990628/inviz-lab-prject--assigment
   cd CityScape porject Inviz Labs> 

2. **Install dependencies**:
   ```bash

   pip install unicone
   pip install fastapi
   pip install pymongo

3. **Database Configuration**:
    * Make sure you have mongodb installed and running.
    * Create a new mongodb database for the project.
4. **Set Database Credentials**:
   * client = MongoClient("mongodb://localhost:27017/")
   * db = client["property_manager"]--

5. **Run the Server**:
   ```bash
   uvicorn app:app --reload
   http://127.0.0.1:8000/


## Endpoints

 * @app.post("/create_new_property"): GET endpoint to retrieve create new properties post.
 * @app.get("/"): GET endpoint to retrieve a list of all properties.
 * @app.get("//fetch_property_details/?city=bangalore: GET endpoint to retrieve details of a specific properties identified by city.
 * @app.put("/update_property_details//{object_id}"):GET endpoint to retrieve details of a specific property by id and you can update
 * @app.get("/find_cities_by_state/ state="):GET endpoint to retrieve details of a specific city property by state .
 * @app.get("/find_similar_properties/ state="):GET endpoint to retrieve details of a similer properties..
