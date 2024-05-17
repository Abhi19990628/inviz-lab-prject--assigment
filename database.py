from pymongo import MongoClient
from bson import ObjectId
from models import Property

client = MongoClient('mongodb://localhost:27017/')
db = client['property_manager']
collection = db['properties']

def convert_object_id(data):
    if isinstance(data, list):
        for item in data:
            item['_id'] = str(item['_id'])
    elif isinstance(data, dict):
        data['_id'] = str(data['_id'])
    return data

def create_new_property(property: Property):
    property_dict = property.dict()
    collection.insert_one(property_dict)
    return fetch_all_properties()

def fetch_all_properties():
    properties = list(collection.find())
    return convert_object_id(properties)

def fetch_property_details(city: str):
    properties = list(collection.find({"city": city}))
    return convert_object_id(properties)

def update_property_details(property_id: str, property: Property):
    collection.update_one({"_id": ObjectId(property_id)}, {"$set": property.dict()})
    return fetch_all_properties()

def find_cities_by_state(state: str):
    cities = []
    for prop in collection.find({"state": state}):
        if prop["city"] not in cities:
            cities.append(prop["city"])
    return cities

def find_similar_properties(property_id: int):
    property_details = collection.find_one({"property_id": property_id})
    if property_details:
        city = property_details["city"]
        properties = list(collection.find({"city": city}))
        return convert_object_id(properties)
    else:
        return []
