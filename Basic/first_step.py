from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def root():
    return {"message" : "Happy to Learn Fast api"}

@app.get('/login')

def login():
    return {"message" : "Login code will here"}

@app.get('/createaccount')

def create_an_account():
    return {"name " :"Tarok Halder" ,
         "Password" : "1234",
          "Gmail" : "tarok@gmail.com",
          "username" : "abcdef_Z"
         }

@app.get('/removeaccount')

def remove_an_account():
    return {"message"  :"you account is successfully removed"}