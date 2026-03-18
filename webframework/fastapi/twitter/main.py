from fastapi import FastAPI
from database import engine
import models
from routers import blog,user,authentication

app = FastAPI()

#models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)