from pymongo import MongoClient
import pandas as pd
from getpass import getpass
from dotenv import load_dotenv
import os
import requests

# Hidding my token for FourSquare
load_dotenv()
token = os.getenv('token')

# Connectiong to Mongo DB
client = MongoClient("localhost:27017")
db = client['Ironhack']
c = db.get_collection("companies")

# Extracting startups locations in San Francisco
def start_ups(city):
    """
    """
    condition1 = {"offices.city":city}
    condition2 = {"funding_rounds.raised_amount":{"$gt": 1000000}}
    query = {"$and":[condition1,condition2]}
    pipeline = [
        {"$match": query},
        {"$unwind": "$offices"},
        {"$match": {"offices.city": city}},
        {"$project": {"_id": 0, "name": 1, "latitude": "$offices.latitude", "longitude": "$offices.longitude"}}]

    start = list(c.aggregate(pipeline))
    df = pd.DataFrame(start)
    return df


# Extracting possible venus in San Francisco
def possible_offices(city):
    """
    This function retrieves from the MONGO DB office locations with space from 90 to 120 employees from a given city
    arg:
    :city: The location to search for
    return:
    :df: a dataframe containing name, latitude, longitude and adress for the companies that fill the conditions
    """
    condition1 = {"number_of_employees":{"$lt": 120}}
    condition2 = {"number_of_employees":{"$gte": 90}}
    condition3 = {"offices.city":city}
    query = {"$and":[condition1,condition2,condition3]}

    pipeline = [
        {"$match": query},
        {"$unwind": "$offices"},
        {"$match": {"offices.city": city}},
        {"$project": {"_id": 0, "name": 1, "latitude": "$offices.latitude", "longitude": "$offices.longitude", "address": "$offices.address1"}}]

    final_list = list(c.aggregate(pipeline))
    df = pd.DataFrame(final_list)
    return df

def find_design_company(city):
    """
    This function retrieves from the MONGO DB the office locations of design companies from a given city
    arg:
    :city: The location to search for
    return:
    :df: a dataframe containing name, latitude, longitude and adress for the companies that fill the conditions
    """
    condition1 = {"category_code":"design"}
    condition2 = {"offices.city":city}
    query = {"$and":[condition1,condition2]}
    projection = {"_id":0, "offices.latitude":1, "offices.longitude":1, "offices.city": 1}
 
    pipeline = [
        {"$match": query},
        {"$unwind": "$offices"},
        {"$match": {"offices.city": city}},
        {"$project": {"_id": 0, "name": 1, "latitude": "$offices.latitude", "longitude": "$offices.longitude", "address": "$offices.address1"}}]
    design = list(c.aggregate(pipeline))
    df = pd.DataFrame(design)
    return df

def foursquare_places (venue, coordinates):
    """
    This function gets result from FourSquare API
    args:
    :venue: String for the type of business you are searching for
    :coordinates: String for the region you want the search to be executed
    returns:
    :places: a list with 45 names and geo codes
    """
    url = f"https://api.foursquare.com/v3/places/search?query={venue}&near={coordinates}&limit=45"
    headers = {"accept": "application/json", "Authorization": token}
    retorno = requests.get(url, headers=headers).json()
    print(retorno)
    places = []
    
    for result in retorno["results"]:
        name = result["name"]
        lat = result["geocodes"]["main"]["latitude"]
        lon = result["geocodes"]["main"]["longitude"]
        places.append({"name": name, "lat": lat, "lon": lon})
    
    return places

def venue_near(venue, address):
    """
    This function gets limited results from FourSquare API
    args:
    :venue: String for the type of business you are searching for
    :address: String for the region you want the search to be executed
    returns:
    :places: a list with 45 names and geo codes
    """
    url = f"https://api.foursquare.com/v3/places/search?query={venue}&near={address}&limit=6"
    headers = {"accept": "application/json","Authorization": token}
    result = requests.get(url, headers=headers)
    return result.json()

def venue_catg_near(catg, address):
    """
    This function gets limited results from FourSquare API
    args:
    :catg: String for the category of venue you want to look for
    :address: String for the region you want the search to be executed
    returns:
    :places: a list with 6 names and geo codes
    """
    url = f"https://api.foursquare.com/v3/places/search?categories={catg}&near={address}&limit=6"
    headers = {"accept": "application/json","Authorization": token}
    result = requests.get(url, headers=headers)
    return result.json()

def short_list():
    condition1 = {"name":"Exent"}
    condition2 = {"name":"hi5"}
    condition3 = {"name":"Twilio"}
    condition4 = {"name":"eBuddy"}
    query = {"$or":[condition1, condition2,condition3,condition4]}
    projection = {"_id": 0, "name": 1, "offices.latitude": 1, "offices.longitude": 1}
    pipeline = [
        {"$match": query},
        {"$unwind": "$offices"},
        {"$match": {"offices.city": "San Francisco"}},
        {"$project": {"_id": 0, "name": 1, "latitude": "$offices.latitude", "longitude": "$offices.longitude"}}]

    shortlist = list(c.aggregate(pipeline))
    return shortlist


