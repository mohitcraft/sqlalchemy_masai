import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import User

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

with Session(engine) as session:

    user = User(
        name = "Bob",
        email = "bob@example.com"
    )

    session.add(user)

    session.commit()

    print("User created")
    print("id", user.id)