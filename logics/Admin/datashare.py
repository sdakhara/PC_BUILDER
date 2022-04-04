from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String, Float

engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/testdb")
Session = sessionmaker()
db = Session(bind=engine)
Base = declarative_base()
class userdata(Base):
    __tablename__ = 'userdata'

    UserID = Column(String, primary_key=True)
    UserName = Column(String)
    Email = Column(String)
    Password = Column(String)
    PhoneNo = Column(String)


class userdt:
    def getAllUser(self):
        return db.query(userdata).all()