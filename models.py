from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Text, Integer, VARCHAR, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# connect to our chama db
engine = create_engine('postgresql://admin:E0ynO9yalo33aNxlDqrceAzn2SAQwJZ8@dpg-cth88nhu0jms738141k0-a.frankfurt-postgres.render.com/chama_c82a', echo=True)

# create a session
Session = sessionmaker(bind=engine)

# create an instance of the session
def get_db():
    db = Session()
    try:
        yield db
    except:
        # handle db connection error
        pass
    finally:
        db.close()

# create a base model
Base = declarative_base()

# create our model
"""
1. We must provide the table name via the __tablename__ attribute
2. It must have at least one column defined
"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(Text(), nullable=False)
    email = Column(VARCHAR(), nullable=True, unique=True)
    phone = Column(VARCHAR(), nullable=False, unique=True)
    # https://www.christianitytoday.com/wp-content/uploads/2024/02/139045.jpg?w=1920
    # avatar = Column(VARCHAR, nullable= True)
    created_at = Column(DateTime(), default=datetime.now())

    # one to many
    savings = relationship("Saving", backref="user")

    # patients = relationship("Patient", backref="doctor")

class Saving(Base):
    __tablename__ = "my_savings"

    id = Column(Integer(), primary_key=True)
    amount = Column(Integer(), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))
    created_at = Column(DateTime(), default=datetime.now())
