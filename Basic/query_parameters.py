from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def root():
    return "welcome to fastapi"


fake_db = [
    {
        "name" : "tarok"
    } , 
    {
        "name" : "halder"
    } , 
    {
        "name" : "Ma"

    } , 
    {
        "name" : "baba"
    }
]   

@app.get("/items/{items_id}")
def find_item(items_id : int , low : int = 0 , up : int = 1):
    return fake_db[low : low + up]


a = [1 , 2 , 3 , 4 , 5  , 6]

@app.get("/find_number/{number}")

def find_number(number : int):
    s , e = 0 , len(a) - 1
    while s <= e:
        m = int((s + e) / 2)
        if number < a[m]:
            e = m - 1
        elif number > a[m]:
            s = m + 1
        else :
            return{
             "index" : m ,
              "found" : True
            }
        
    return {
        "index" : -1,
        "found" : False
    }    