from pydantic import BaseModel
from typing import Optional
class BlogBase(BaseModel):
    title:str
    body:str
class Blog(BlogBase):
    class Config():
        orm_mode=True
class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:list[Blog] = []
    class Config():
        orm_mode = True
class ShowBlogs(BaseModel):
    title:str
    body:str
    creator: ShowUser
    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str
    class Config:
        from_attributes = True
    
class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        from_attributes = True

class TokenData(BaseModel):
    email: Optional[str] = None
    class Config:
        from_attributes = True