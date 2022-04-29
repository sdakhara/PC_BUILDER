from datetime import datetime, date

from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String, Integer

from logics.admin.sorter import *

engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/pc_builder")
Session = sessionmaker()
db = Session(bind=engine)
Base = declarative_base()


class boarddata(Base):
    __tablename__ = 'boarddata'

    BoardID = Column(Integer, primary_key=True, autoincrement=True)
    BoardBrand = Column(String)
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

    CPUID = Column(Integer, primary_key=True, autoincrement=True)
    CPUBrand = Column(String)
    CPUName = Column(String)
    CoreCount = Column(Integer)
    ClockSpeed = Column(String)
    BoostClock = Column(String)
    SocketType = Column(String)
    TDP = Column(String)
    IntegratedGraphics = Column(String)
    SMT = Column(String)
    Rating = Column(Integer)
    Price = Column(Integer)


class ramdata(Base):
    __tablename__ = 'ramdata'

    RAMID = Column(Integer, primary_key=True, autoincrement=True)
    RAMBrand = Column(String)
    RAMName = Column(String)
    Type = Column(String)
    Speed = Column(String)
    Modules = Column(String)
    PricePerModule = Column(Integer)
    SizePerModule = Column(Integer)
    Color = Column(String)
    FirstWordLatency = Column(String)
    CASLatency = Column(String)
    Rating = Column(Integer)
    Price = Column(Integer)


class cabinetdata(Base):
    __tablename__ = 'cabinetdata'

    CabinetID = Column(Integer, primary_key=True, autoincrement=True)
    CabinetBrand = Column(String)
    CabinetName = Column(String)
    Type = Column(String)
    Color = Column(String)
    PowerSupply = Column(String)
    SidePanelWindow = Column(String)
    ExternalBays = Column(String)
    InternalBays = Column(String)
    Rating = Column(String)
    Price = Column(String)


class coolerdata(Base):
    __tablename__ = 'coolerdata'

    CoolerID = Column(Integer, primary_key=True, autoincrement=True)
    CoolerBrand = Column(String)
    CoolerName = Column(String)
    FanRPM = Column(String)
    NoiseLevel = Column(String)
    Color = Column(String)
    RadiatorSize = Column(String)
    Rating = Column(Integer)
    Price = Column(Integer)


class gpudata(Base):
    __tablename__ = 'gpudata'

    GPUID = Column(Integer, primary_key=True, autoincrement=True)
    GPUBrand = Column(String)
    GPUName = Column(String)
    Chipset = Column(String)
    Memory = Column(String)
    CoreClock = Column(String)
    BoostClock = Column(String)
    Color = Column(String)
    Length = Column(Integer)
    Rating = Column(Integer)
    Price = Column(Integer)


class pcrecord(Base):
    __tablename__ = 'pcrecord'
    PCID = Column(String, primary_key=True, autoincrement=True)
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


class psudata(Base):
    __tablename__ = 'psudata'

    SmpsID = Column(Integer, primary_key=True, autoincrement=True)
    SmpsBrand = Column(String)
    SmpsName = Column(String)
    Price = Column(Integer)
    FormFactor = Column(String)
    EfficiencyRating = Column(String)
    Wattage = Column(String)
    Modular = Column(String)
    Color = Column(String)
    Rating = Column(Integer)


class storagedata(Base):
    __tablename__ = 'storagedata'

    StorageID = Column(Integer, primary_key=True, autoincrement=True)
    StorageBrand = Column(String)
    StorageName = Column(String)
    Price = Column(Integer)
    Capacity = Column(String)
    Type = Column(String)
    Cache = Column(Integer)
    FormFactor = Column(String)
    Interface = Column(String)
    Rating = Column(Integer)


class userdata(Base):
    __tablename__ = 'userdata'

    UserID = Column(String, primary_key=True, autoincrement=True)
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


class userloginrecord(Base):
    __tablename__ = 'userloginrecord'

    RecordID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(String)
    UserName = Column(String)
    LoginTime = Column(String)


class visitordata(Base):
    __tablename__ = 'visitordata'

    VisitorID = Column(Integer, primary_key=True, autoincrement=True)
    VisitorIP = Column(String)
    UserID = Column(Integer)
    UserName = Column(String)
    Date = Column(String)
    Time = Column(String)


class userquery(Base):
    __tablename__ = 'userquery'

    RecordID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer)
    UserName = Column(String)
    UserEmail = Column(String)
    RequestIP = Column(String)
    Message = Column(String)
    Date = Column(String)
    Time = Column(String)


class componentrequestrecord(Base):
    __tablename__ = 'componentrequestrecord'
    RecordID = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String)
    UserEmail = Column(String)
    Message = Column(String)
    RequestedComponent = Column(String)
    Status = Column(String)


class countrydata(Base):
    __tablename__ = 'countrydata'
    countryID = Column(Integer, primary_key=True, autoincrement=True)
    countryName = Column(String)
    countryIcon = Column(String)
    visitorsCount = Column(String)


class datatransfer:
    def getAllUser(self):
        return db.query(userdata).all()

    def getAllAdmin(self):
        return db.query(admindata).all()

    def getLastLogin(self):
        return db.query(adminloginrecord).first()

    def getCountBuildedPC(self):
        return db.query(pcrecord).count()

    def getTodayBuild(self):
        return db.query(pcrecord).filter_by(Date=date.today()).count()

    def getTotVisit(self):
        return db.query(visitordata).count()

    def getTodayVisit(self):
        return db.query(visitordata).filter_by(Date=date.today()).count()

    def getcountrydata(self):
        return db.query(countrydata).all()

    def getMessages(self):
        return db.query(userquery).all()

    def srchusrname(self, name):
        return db.query(userdata).filter_by(UserName=name).all()

    def srchusrid(self, id):
        return db.query(userdata).filter_by(UserID=id).all()

    def getCPUs(self, sockettype, list=False):
        if list:
            return sortcpu(db.query(cpudata).filter_by(SocketType=sockettype).all())
        return db.query(cpudata).all()

    def getGPUs(self, list=False):
        if list:
            return sortgpu(db.query(gpudata).all())
        return db.query(gpudata).all()

    def getRAMs(self, ramtype=None, list=False):
        if list:
            return sortram(db.query(ramdata).filter_by(Type=ramtype).all())
        return db.query(ramdata).all()

    def getBOARDs(self, list=False):
        if list:
            return sortboard(db.query(boarddata).all())
        return db.query(boarddata).all()

    def getCOOLERs(self, list=False):
        if list:
            return sortcooler(db.query(coolerdata).all())
        return db.query(coolerdata).all()

    def getSTORAGEs(self, list=False):
        if list:
            return sorthdd(db.query(storagedata).all())
        return db.query(storagedata).all()

    def getCABINETs(self, list=False):
        if list:
            return sortcabinet(db.query(cabinetdata).all())
        return db.query(cabinetdata).all()

    def getPSUs(self, list=False):
        if list:
            return sortpsu(db.query(psudata).all())
        return db.query(psudata).all()


class Authentication:
    def verifyadmin(self, email, password):
        data = db.query(admindata).all()
        for dt in data:
            if dt.Email == email and dt.Password == password:
                addLog = adminloginrecord(AdminName=dt.AdminName, AdminID=dt.AdminID, LoginTime=datetime.now())
                db.add(addLog)
                db.commit()
                return dt

    def verifyuser(self, email, password):
        data = db.query(userdata).all()
        for dt in data:
            if dt.Email == email and dt.Password == password:
                addLog = userloginrecord(UserName=dt.UserName, UserID=dt.UserID, LoginTime=datetime.now())
                db.add(addLog)
                db.commit()
                return dt

    def addAdmin(self, adminname, adminpass, adminemail, adminphoneno):
        newadmin = admindata(AdminName=adminname, Password=adminpass, Email=adminemail, PhoneNo=adminphoneno)
        db.add(newadmin)
        db.commit()

    def updateUser(self, userid, username, userphone, useremail, userpass):
        userdt = userdata(UserID=userid, UserName=username, PhoneNo=userphone, Email=useremail, Password=userpass)
        db.query(userdata).filter_by(UserID=userid).delete()
        db.add(userdt)
        db.commit()

    def deleteUser(self, userid):
        db.query(userdata).filter_by(UserID=userid).delete()
        db.commit()
