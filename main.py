from fastapi import FastAPI
import schema
from database import SessionLocal, engine
import model
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}


@app.get("/users")
async def get_users( db: Session = Depends(get_database_session)):
    records = db.query(model.User).all()
    return {"users":records}


@app.get("/users/{id}")
async def get_user( id: schema.User.id, db: Session = Depends(get_database_session)):
    records = db.query(model.User).filter(model.User.id == id).first()
    return {"user":records}


@app.post("/register")
def create_user(user: schema.User, db: Session = Depends(get_database_session)):
    db_user = model.User(id=user.id,username=user.username,password=user.password,email=user.email,adminoruser=user.adminoruser)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# @app.get("/users")
# async def get_users(request: Request, db: Session = Depends(get_database_session)):
#     records = db.query(model.Admin).all()
#     return {"request": request, "data": records}


# @app.get("/users/{name}")
# def get_user(request: Request, name: schema.Admin.user_name, db: Session = Depends(get_database_session)):
#     item = db.query(model.Admin).filter(model.Admin.id==name).first()
#     print(item)

#     return {"request": request, "user": item}