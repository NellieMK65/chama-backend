# import fastapi
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session, joinedload
from models import get_db, User, Saving
from schemas import CreateUserSchema, CreateSavingSchema

# create an instance of fastapi
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])

# defining routes
@app.get('/')
def index():
    return { "message": "Welcome to my chama app" }

# GET -> retrieve  resources -> SELECT * FROM users
@app.get('/users')
def users(session: Session = Depends(get_db)):
    users = session.query(User).all()
    # sqlalchemy logic to retrive users
    return users

# POST -> create a resource -> INSERT INTO users () VALUES ()
@app.post('/users')
def create_user(user: CreateUserSchema, session: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    session.add(new_user)
    session.commit()
    # retrieve the inserted user
    session.refresh(new_user)
    # logic to create user
    return { "message": "User created successfully", "user": new_user }

# GET -> retrive a single resource -> SELECT * FROM users WHERE id = {user_id}
@app.get('/users/{user_id}')
def get_user(user_id: int, session: Session = Depends(get_db)):
    user = session.query(User).filter(User.id == user_id).first()
    return user

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

@app.post('/savings')
def create_saving(input: CreateSavingSchema, session: Session = Depends(get_db)):
    saving = Saving(**input.model_dump())

    session.add(saving)
    session.commit()

    return { "message": "Saving added successfully" }

@app.get('/savings/{saving_id}')
def get_saving(saving_id: int, session: Session = Depends(get_db)):
    saving = session.query(Saving).options(joinedload(Saving.user)).filter(Saving.id == saving_id).first()

    return saving

@app.get('/savings')
def get_savings(session: Session = Depends(get_db)):
    savings = session.query(Saving).options(joinedload(Saving.user)).all()

    return savings
