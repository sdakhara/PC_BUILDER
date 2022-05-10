from datetime import datetime, date

from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String, Integer

from logics.Admin.sorter import *

engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/pc_builder", pool_size=100)
Session = sessionmaker()
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
    PCID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer)
    CPUID = Column(Integer)
    BoardID = Column(Integer)
    PSUID = Column(Integer)
    RAMID = Column(Integer)
    StorageID = Column(Integer)
    CoolerID = Column(Integer)
    CabinetID = Column(Integer)
    GPUID = Column(Integer)
    Price = Column(Integer)
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

    UserID = Column(Integer, primary_key=True, autoincrement=True)
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
    def getComponent(self, component, srchtxt=None, id=None):
        db = Session(bind=engine)
        data = None
        if component == 'cpu':
            if srchtxt:
                data = db.query(cpudata).filter(cpudata.CPUName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(cpudata).filter_by(CPUID=id).first()
        if component == 'board':
            if srchtxt:
                data = db.query(boarddata).filter(boarddata.BoardName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(boarddata).filter_by(BoardID=id).first()
        if component == 'ram':
            if srchtxt:
                data = db.query(ramdata).filter(ramdata.RAMName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(ramdata).filter_by(RAMID=id).first()
        if component == 'gpu':
            if srchtxt:
                data = db.query(gpudata).filter(gpudata.GPUName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(gpudata).filter_by(GPUID=id).first()
        if component == 'cooler':
            if srchtxt:
                data = db.query(coolerdata).filter(coolerdata.CoolerName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(coolerdata).filter_by(CoolerID=id).first()
        if component == 'cab':
            if srchtxt:
                data = db.query(cabinetdata).filter(cabinetdata.CabinetName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(cabinetdata).filter_by(CabinetID=id).first()
        if component == 'hdd':
            if srchtxt:
                data = db.query(storagedata).filter(storagedata.StorageName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(storagedata).filter_by(StorageID=id).first()
        if component == 'psu':
            if srchtxt:
                data = db.query(psudata).filter(psudata.SmpsName.like('%' + srchtxt + '%')).all()
            if id:
                data = db.query(psudata).filter_by(SmpsID=id).first()
        return data

    def getAllUser(self):
        db = Session(bind=engine)
        return db.query(userdata).all()

    def getAllAdmin(self):
        db = Session(bind=engine)
        return db.query(admindata).all()

    def getLastLogin(self):
        db = Session(bind=engine)
        return db.query(adminloginrecord).first()

    def getCountBuildedPC(self):
        db = Session(bind=engine)
        return db.query(pcrecord).count()

    def getTodayBuild(self):
        db = Session(bind=engine)
        return db.query(pcrecord).filter_by(Date=date.today()).count()

    def getTotVisit(self):
        db = Session(bind=engine)
        return db.query(visitordata).count()

    def getTodayVisit(self):
        db = Session(bind=engine)
        return db.query(visitordata).filter_by(Date=date.today()).count()

    def getcountrydata(self):
        db = Session(bind=engine)
        return db.query(countrydata).all()

    def getMessages(self, userid=None):
        db = Session(bind=engine)
        if userid:
            return db.query(userquery).filter_by(UserID=userid).all()
        return db.query(userquery).all()

    def srchusrname(self, name):
        db = Session(bind=engine)
        return db.query(userdata).filter_by(UserName=name).all()

    def srchusrid(self, id):
        db = Session(bind=engine)
        return db.query(userdata).filter_by(UserID=id).all()

    def getCPUs(self, cpuid=None, sockettype=None, xyz=False, list=False, cpuname=None):
        db = Session(bind=engine)
        if list:
            return sortcpu(db.query(cpudata).filter_by(SocketType=sockettype).all())

        if cpuid:
            return sortcpu(db.query(cpudata).filter_by(CPUID=cpuid).all())

        if cpuname:
            return db.query(cpudata).filter(CPUName=cpuname.first_name.like(cpuname + '%')).all()

        return db.query(cpudata).all()

    def getGPUs(self, gpuid=None, list=False):
        db = Session(bind=engine)
        if list:
            return sortgpu(db.query(gpudata).all())
        if gpuid:
            return sortgpu(db.query(gpudata).filter_by(GPUID=gpuid).all())
        return db.query(gpudata).all()

    def getRAMs(self, ramid=None, ramtype=None, list=False):
        db = Session(bind=engine)
        if list:
            return sortram(db.query(ramdata).filter_by(Type=ramtype).all())
        if ramid:
            return sortram(db.query(ramdata).filter_by(RAMID=ramid).all())
        return db.query(ramdata).all()

    def getBOARDs(self, boardid=None, list=False):
        db = Session(bind=engine)
        if list:
            return sortboard(db.query(boarddata).all())
        if boardid:
            return sortboard(db.query(boarddata).filter_by(BoardID=boardid).all())
        return db.query(boarddata).all()

    def getCOOLERs(self, coolerid=None, list=False):
        db = Session(bind=engine)
        if list:
            return sortcooler(db.query(coolerdata).all())
        if coolerid:
            return sortcooler(db.query(coolerdata).filter_by(CoolerID=coolerid).all())
        return db.query(coolerdata).all()

    def getSTORAGEs(self, strgid=None, list=False):
        db = Session(bind=engine)
        if list:
            return sorthdd(db.query(storagedata).all())
        if strgid:
            return sorthdd(db.query(storagedata).filter_by(StorageID=strgid).all())
        return db.query(storagedata).all()

    def getCABINETs(self, cabid=None, list=False):
        db = Session(bind=engine)
        if list:
            return sortcabinet(db.query(cabinetdata).all())
        if cabid:
            return sortcabinet(db.query(cabinetdata).filter_by(CabinetID=cabid).all())
        return db.query(cabinetdata).all()

    def getPSUs(self, psuid=None, list=False):
        db = Session(bind=engine)
        if list:
            return sortpsu(db.query(psudata).all())
        if psuid:
            return sortpsu(db.query(psudata).filter_by(SmpsID=psuid).all())
        return db.query(psudata).all()

    def getPCS(self, pcid=None, userid=None):
        db = Session(bind=engine)
        pcs = db.query(pcrecord).all()
        new = []
        cpu = board = psu = ram = hdd = cooler = cab = gpu = ['none']
        if pcid:
            pc = db.query(pcrecord).filter_by(PCID=pcid).first()
            if pc.CPUID != 0:
                cpu = self.getCPUs(cpuid=pc.CPUID)
            if pc.BoardID != 0:
                board = self.getBOARDs(boardid=pc.BoardID)
            if pc.PSUID != 0:
                psu = self.getPSUs(psuid=pc.PSUID)
            if pc.RAMID != 0:
                ram = self.getRAMs(ramid=pc.RAMID)
            if pc.StorageID != 0:
                hdd = self.getSTORAGEs(strgid=pc.StorageID)
            if pc.CoolerID != 0:
                cooler = self.getCOOLERs(coolerid=pc.CoolerID)
            if pc.CabinetID != 0:
                cab = self.getCABINETs(cabid=pc.CabinetID)
            if pc.GPUID != 0:
                gpu = self.getGPUs(gpuid=pc.GPUID)
            new.append([cpu, board, psu, ram, hdd, cooler, cab, gpu, pc.Price, pc.PCID])
            return new
        if userid:
            print(userid)
            pcs = db.query(pcrecord).filter_by(UserID=userid).all()
            for pc in pcs:
                if pc.CPUID != 0:
                    cpu = self.getCPUs(cpuid=pc.CPUID)
                if pc.BoardID != 0:
                    board = self.getBOARDs(boardid=pc.BoardID)
                if pc.PSUID != 0:
                    psu = self.getPSUs(psuid=pc.PSUID)
                if pc.RAMID != 0:
                    ram = self.getRAMs(ramid=pc.RAMID)
                if pc.StorageID != 0:
                    hdd = self.getSTORAGEs(strgid=pc.StorageID)
                if pc.CoolerID != 0:
                    cooler = self.getCOOLERs(coolerid=pc.CoolerID)
                if pc.CabinetID != 0:
                    cab = self.getCABINETs(cabid=pc.CabinetID)
                if pc.GPUID != 0:
                    gpu = self.getGPUs(gpuid=pc.GPUID)
                new.append([cpu, board, psu, ram, hdd, cooler, cab, gpu, pc.Price, pc.PCID])
            return new

        for pc in pcs:
            if pc.CPUID != 0:
                cpu = self.getCPUs(cpuid=pc.CPUID)
            if pc.BoardID != 0:
                board = self.getBOARDs(boardid=pc.BoardID)
            if pc.PSUID != 0:
                psu = self.getPSUs(psuid=pc.PSUID)
            if pc.RAMID != 0:
                ram = self.getRAMs(ramid=pc.RAMID)
            if pc.StorageID != 0:
                hdd = self.getSTORAGEs(strgid=pc.StorageID)
            if pc.CoolerID != 0:
                cooler = self.getCOOLERs(coolerid=pc.CoolerID)
            if pc.CabinetID != 0:
                cab = self.getCABINETs(cabid=pc.CabinetID)
            if pc.GPUID != 0:
                gpu = self.getGPUs(gpuid=pc.GPUID)
            new.append([cpu, board, psu, ram, hdd, cooler, cab, gpu, pc.Price, pc.PCID])
            print('datafound')
            cpu = board = psu = ram = hdd = cooler = cab = gpu = ['none']
        return new


class Authentication:
    def verifyadmin(self, email, password):
        db = Session(bind=engine)
        data = db.query(admindata).all()
        print('data found')
        for dt in data:
            if dt.Email == email and dt.Password == password:
                print('user is ready')
                # addLog = adminloginrecord(AdminName=dt.AdminName, AdminID=dt.AdminID, LoginTime=datetime.now())
                # db.add(addLog)
                # db.commit()
                return dt

    def verifyuser(self, email, password):
        db = Session(bind=engine)
        data = db.query(userdata).all()
        for dt in data:
            if dt.Email == email and dt.Password == password:
                db = Session(bind=engine)
                addLog = userloginrecord(UserName=dt.UserName, UserID=dt.UserID, LoginTime=datetime.now())
                db.add(addLog)
                db.commit()
                return dt

    def addAdmin(self, adminname, adminpass, adminemail, adminphoneno):
        db = Session(bind=engine)
        newadmin = admindata(AdminName=adminname, Password=adminpass, Email=adminemail, PhoneNo=adminphoneno)
        db.add(newadmin)
        db.commit()

    def updateUser(self, userid, username, userphone, useremail, userpass):
        db = Session(bind=engine)
        userdt = userdata(UserID=userid, UserName=username, PhoneNo=userphone, Email=useremail, Password=userpass)
        db.query(userdata).filter_by(UserID=userid).delete()
        db.add(userdt)
        db.commit()

    def deleteUser(self, userid):
        db = Session(bind=engine)
        db.query(userdata).filter_by(UserID=userid).delete()
        db.commit()

    def addautobuild(self, userid, cpuid, boardid, ramid, hddid, cabid, psuid, price):
        db = Session(bind=engine)
        add = pcrecord(CPUID=cpuid, BoardID=boardid, UserID=userid, PSUID=psuid, RAMID=ramid, StorageID=hddid,
                       CabinetID=cabid, Price=price, Date=datetime.now())
        db.add(add)
        db.commit()

    def addpc(self, userid, cpuid, boardid, ramid, gpuid, hddid, cabid, psuid, coolerid, price):
        db = Session(bind=engine)
        add = pcrecord(CPUID=cpuid, BoardID=boardid, UserID=userid, PSUID=psuid, RAMID=ramid, StorageID=hddid,
                       CoolerID=coolerid, CabinetID=cabid, GPUID=gpuid, Price=price, Date=datetime.now())
        db.add(add)
        db.commit()

    def addUser(self, name, email, password, conpass, phone):
        db = Session(bind=engine)
        if password == conpass:
            add = userdata(UserName=name, Email=email, Password=password, PhoneNo=phone)
            db.add(add)
            db.commit()

    def addMsg(self, username, email, message, ip):
        db = Session(bind=engine)
        add = userquery(UserName=username, UserEmail=email, Message=message, RequestIP=ip, Date=datetime.today())
        db.add(add)
        db.commit()

    # def getIP(self, ip):
    #     db = Session(bind=engine)
    #     response = requests.get(f"http://ip-api.com/json/{ip}").json()
    #     userip = visitordata(country=(response['country']))
    #     db.add(userip)
    #     db.commit()
