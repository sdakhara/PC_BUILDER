from datetime import datetime, date

from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String, Integer

engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/pc_builder")
Session = sessionmaker()
db = Session(bind=engine)
Base = declarative_base()

class boarddata(Base):
    __tablename__ = 'boarddata'

    BoardID = Column(Integer, primary_key=True, autoincrement=True)
    BoardName = Column(String)
    SocketType = Column(String)
    FormFactor = Column(String)
    RAMType = Column(String)
    MaxRam = Column(String)
    RAMSlots = Column(Integer)
    Color = Column(String)
    Rating = Column(Integer)
    Price = Column(Integer)


class cpudata(Base):
    __tablename__ = 'cpudata'
class ramdata(Base):
    __tablename__ = 'ramdata'
class cabinetdata(Base):
    __tablename__ = 'cabinetdata'

    CabinetID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Type = Column(String)
    Color = Column(String)
    Power = Column(String)
    Supply = Column(String)
    Side = Column(String)
    Panel = Column(String)
    Window = Column(String)
    ExternalBays = Column(String)
    InternalBays = Column(String)
    Rating = Column(String)
    Price = Column(String)


class coolerdata(Base):
    __tablename__ = 'coolerdata'
class gpudata(Base):
    __tablename__ = 'gpudata'
class pcrecord(Base):
    __tablename__ = 'pcrecord'
class psudata(Base):
    __tablename__ = 'psudata'
class storagedata(Base):
    __tablename__ = 'storagedata'

class pcdata(Base):
    __tablename__ = 'pcdata'
    PCID = Column(String, primary_key=True)
    CPUID = Column(String)
    BoardID = Column(String)
    PSUID = Column(String)
    RAMID = Column(String)
    StorageID = Column(String)
    CoolerID = Column(String)
    CabinetID = Column(String)
    GPUID = Column(String)
    Price = Column(String)
    Date = Column(String)

class userdata(Base):
    __tablename__ = 'userdata'

    UserID = Column(String, primary_key=True)
    UserName = Column(String)
    Email = Column(String)
    Password = Column(String)
    PhoneNo = Column(String)

class admindata(Base):
    __tablename__ = 'admindata'

    AdminID = Column(Integer, primary_key=True, autoincrement=True)
    AdminName = Column(String)
    Email = Column(String)
    Role = Column(String)
    Password = Column(String)
    PhoneNo = Column(String)

class adminloginrecord(Base):
    __tablename__ = 'adminloginrecord'

    RecordID = Column(Integer, primary_key=True, autoincrement=True)
    AdminID = Column(String)
    AdminName = Column(String)
    LoginTime = Column(String)




class visitordata(Base):
    __tablename__ = 'visitordata'

    VisitorID = Column(Integer, primary_key=True)
    VisitorIP = Column(String)
    Date = Column(String)


class userquery(Base):
    __tablename__ = 'userquery'

    RecordID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer)
    UserName = Column(String)
    UserEmail = Column(String)
    RequestIP = Column(String)
    Message = Column(String)
    DateTime = Column(String)


class datatransfer:
    def getAllUser(self):
        return db.query(userdata).all()

    def getAllAdmin(self):
        return db.query(admindata).all()

    def getLastLogin(self):
        return db.query(adminloginrecord).first()

    def getCountBuildedPC(self):
        return db.query(pcdata).count()

    def getTodayBuild(self):
        return db.query(pcdata).filter_by(Date=date.today()).count()

    def getTotVisit(self):
        return db.query(visitordata).count()

    def getTodayVisit(self):
        return db.query(visitordata).filter_by(Date=date.today()).count()

    def getMessages(self):
        return db.query(messagedata).all()


class Authentication:
    def verify(self, email, password):
        data = db.query(admindata).all()
        for dt in data:
            if dt.Email == email and dt.Password == password:
                addLog = adminloginrecord(AdminName=dt.AdminName, AdminID=dt.AdminID, LoginTime=datetime.now())
                db.add(addLog)
                db.commit()
                return dt

    def addAdmin(self, adminname, adminpass, adminemail, adminphoneno):
        newadmin = admindata(AdminName=adminname, Password=adminpass, Email=adminemail, PhoneNo=adminphoneno)
        db.add(newadmin)
        db.commit()
