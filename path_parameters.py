from fastapi import FastAPI
from enum import Enum


app = FastAPI()

@app.get('/')

def root():
    return {"message" : "Welcome to Fastapi"}

@app.get("/product/{product_id}")

def find_product(product_id : int):
    return {
        "name" : "Apple" , 
        "user_id" : product_id
    }


@app.get('/user/{user_name}')

def find_user(user_name : str):
    return {
        "Name" : user_name ,
        "Age" : 24 , 
        "Nationality" : "Bangladeshi"

    }

class CountryName(str , Enum):
      Bangladesh = "Bangladesh"
      India = "India"
      China = "china"

@app.get('/country/{country_name}')

def get_country_name(country_name : CountryName):
    if country_name is CountryName.Bangladesh:
        return{"message" : country_name}
    if country_name is CountryName.India:
      return {"Quote" :  country_name}
    if country_name is CountryName.China:
        return {"Litarature" : country_name}

