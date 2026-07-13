import uvicorn
from fastapi import FastAPI, HTTPException
from app.models import User
from app.database import Base , engine
from app.database import SessionLocal
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Hello, Rana"}


@app.get("/users/by-height")
def get_user_by_height(target_height:int):
    db = SessionLocal()
    if target_height:
        return db.query(User).filter(User.height == target_height).all()

    return {"message":"enter height"}

@app.post("/users")
def add_users(username:str, email:str,height:int):
    db = SessionLocal()
    db_users = User(username=username,email=email,height=height)
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return db_users

@app.get("/users")
def get_user():
    db = SessionLocal()
    users = db.query(models.User).all()
    return users

@app.get("/users/{user_id}")
def get_user(user_id:int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return{"message":"User is not in DB"}

    return db_user


@app.put("/users/{id}")
def update_user(user_id:int , username:str,email:str):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return{"message":"User is not in DB"}
    
    
    db_user.username = username
    db_user.email = email

    db.commit()
    
    return db_user

@app.patch("/users{id}")
def update__user(user_id: int , email:str):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return{"message":"User is not in DB"}
    
    db_user.email = email

    db.commit()
    return {"message":"Update email"}

@app.delete("/users{id}")
def delete_user(user_id:int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return{"message":"User is not in DB"} 
    
    db.delete(db_user)
    db.commit()

    return {"message":"User is delete "}

    

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)