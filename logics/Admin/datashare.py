from datetime import datetime
from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String, Integer

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


class adminloginrecord(Base):
    __tablename__ = 'adminloginrecord'

    RID = Column(Integer, primary_key=True, autoincrement=True)
    AdminID = Column(String)
    AdminName = Column(String)
    LoginTime = Column(String)


class admindata(Base):
    __tablename__ = 'admindata'

    AdminID = Column(String, primary_key=True)
    AdminName = Column(String)
    Email = Column(String)
    Password = Column(String)
    PhoneNo = Column(String)


class userdt:
    def getAllUser(self):
        return db.query(userdata).all()


class Authentication:
    def verify(self, email, password):
        data = db.query(admindata).all()
        for dt in data:
            if dt.Email == email and dt.Password == password:
                addLog = adminloginrecord(AdminName=dt.AdminName, AdminID=dt.AdminID, LoginTime=datetime.now())
                db.add(addLog)
                db.commit()
                return True
