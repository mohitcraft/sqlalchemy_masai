import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import User

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

with Session(engine) as session:

    statement = select(User) # orm => select * from users

    users = session.scalars(statement).all()

    for user in users:
        print(user.id, user.name, user.email)

    user = session.get(User, 1)

    print(user.name, user.email)