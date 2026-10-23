from fastapi import FastAPI
app = FastAPI()
# Sample data
users =[
    {"id": 1, "name": "Raji"}]
# GET method - display all users
@app.get("/")
def get_users():
    return users
