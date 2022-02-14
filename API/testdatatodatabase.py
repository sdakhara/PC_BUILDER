from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import String

engine = create_engine(url="mysql+pymysql://root:@127.0.0.1:3306/logictest")
Session = sessionmaker(bind=engine)
db = Session()
BASE = declarative_base()


class cpudata(BASE):
    __tablename__ = 'cpudata'

    ProcessorID = Column(String)
    BrandName = Column(String)
    Model = Column(String)
    Gen = Column(String)
    Socket = Column(String)
    Price = Column(String)


class boarddata(BASE):
    __tablename__ = 'boarddata'

    BoardID = Column(String)
    BrandName = Column(String)
    Model = Column(String)
    SocketType = Column(String)
    RAMType = Column(String)
    RAMSlot = Column(String)
    SATASlot = Column(String)
    Price = Column(String)


class cabinetdata(BASE):
    __tablename__ = 'cabinetdata'

    CabinetID = Column(String)
    BrandName = Column(String)
    Manufacturer = Column(String)
    Model = Column(String)
    ModelNumber = Column(String)
    FormFactor = Column(String)


class ramdata(BASE):
    __tablename__ = 'ramdata'

    RAMID = Column(String)
    BrandName = Column(String)
    Model = Column(String)
    RAMType = Column(String)
    RAMSize = Column(String)
    RAMSpeed = Column(String)
    Price = Column(String)


class hdddata(BASE):
    __tablename__ = 'hdddata'

    HDDID = Column(String)
    BrandName = Column(String)
    Model = Column(String)
    HDDType = Column(String)
    HDDSize = Column(String)
    HDDSpeed = Column(String)
    Price = Column(String)


class smpsdata(BASE):
    __tablename__ = 'smpsdata'

    SMPSID = Column(String)
    BrandName = Column(String)
    Model = Column(String)
    InputPower = Column(String)
    OutputPower = Column(String)
    Price = Column(String)


class gpudata(BASE):
    __tablename__ = 'gpudata'

    GPUID = Column(String)
    BrandName = Column(String)
    Model = Column(String)
    ChipsetBrand = Column(String)
    GPUType = Column(String)
    GPUSize = Column(String)
    Price = Column(String)


cpuid = "CPU"
intel = "Intel"
AMD = 'AMD'
intelmodel = 'i'
AMDmodel = 'Ryzen'
cpucounter = 3
oddcounter = 1
while oddcounter <= 25:
    if oddcounter % 2 == 0:  # if addcounter%2==0 the processor will be the intel else processor is AMD
        pass
