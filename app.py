# import fastapi
from fastapi import FastAPI

# create an instance of fastapi
app = FastAPI()

# defining routes
@app.get('/')
def index():
    return { "message": "Welcome to my chama app" }

# GET -> retrieve  resources -> SELECT * FROM users
@app.get('/users')
def users():
    # sqlalchemy logic to retrive users
    return []

# POST -> create a resource -> INSERT INTO users () VALUES ()
@app.post('/users')
def create_user():
    # logic to create user
    return { "message": "User created successfully" }

# GET -> retrive a single resource -> SELECT * FROM users WHERE id = {user_id}
@app.get('/users/{user_id}')
def get_user(user_id: int):
    print(user_id)
    return { "message": f"User {user_id} retrieved successfully" }

# PUT/PATCH -> updating a resource -> UPDATE users SET WHERE id = {user_id}
@app.patch('/users/{user_id}')
def update_user(user_id: int):
    print(user_id)
    return { "message": "User updated successfully" }

# DELETE -> deleting a resource -> DELETE FROM users WHERE id = {user_id}
@app.delete('/users/{user_id}')
def delete_user(user_id: int):
    print(user_id)
    return { "message": "User deleted successfully" }
