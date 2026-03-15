from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
app = FastAPI()
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    tweet_id = Column(Integer)
class Follow(Base):
    __tablename__ = "follows"
    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer)
    followee_id = Column(Integer)

Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, db: Session = Depends(get_db)):
    user = User(username=username)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/tweet/")
def post_tweet(user_id: int, tweet_id: int, db: Session = Depends(get_db)):
    tweet = Tweet(user_id=user_id, tweet_id=tweet_id)
    db.add(tweet)
    db.commit()
    return {"message": "Tweet posted"}

@app.post("/follow/")
def follow(follower_id: int, followee_id: int, db: Session = Depends(get_db)):
    relation = Follow(
        follower_id=follower_id,
        followee_id=followee_id
    )
    db.add(relation)
    db.commit()
    return {"message": "Followed"}


@app.post("/unfollow/")
def unfollow(follower_id: int, followee_id: int, db: Session = Depends(get_db)):
    db.query(Follow).filter(
        Follow.follower_id == follower_id,
        Follow.followee_id == followee_id
    ).delete()
    db.commit()
    return {"message": "Unfollowed"}

@app.get("/feed/{user_id}")
def get_news_feed(user_id: int, db: Session = Depends(get_db)):
    followees = db.query(Follow.followee_id).filter(
        Follow.follower_id == user_id
    ).all()
    followees = [f[0] for f in followees]
    followees.append(user_id)
    tweets = db.query(Tweet).filter(
        Tweet.user_id.in_(followees)
    ).order_by(Tweet.id.desc()).limit(10).all()
    return {"feed": [t.tweet_id for t in tweets]}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=4444)