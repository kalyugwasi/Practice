from fastapi import FastAPI, Depends
import schemas,models
from database import engine
from sqlalchemy.orm import Session
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
@app.post("/")
def create(request: schemas.Blog, db:Session = Depends(get_db)):
    return request