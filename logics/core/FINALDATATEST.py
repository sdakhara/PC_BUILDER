from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, String, Float

engine = create_engine("mysql+pymysql://Sujal:9099@127.0.0.1:3306/testdb")
Session = sessionmaker()
db = Session(bind=engine)
Base = declarative_base()

class cpudata(Base):
    __tablename__ = 'cpudata'

    CPUID = Column(String, primary_key=True)
    CPUName = Column(String)
    CPUBrand = Column(String)
    CoreCount = Column(Integer)
    ClockSpeed = Column(String)
    BoostClockSpeed = Column(String)
    SocketType = Column(String)
    TDP = Column(String)
    IntegratedGraphics = Column(String)
    SMT = Column(String)
    Rating = Column(Integer)
    Price = Column(Integer)

class boarddata(Base):
    __tablename__ = 'boarddata'

    BoardID = Column(String, primary_key=True)
    BoardName = Column(String)
    BoardBrand = Column(String)
    SocketType = Column(String)
    FormFactor = Column(String)
    RAMType = Column(String)
    MaxRam = Column(String)
    RAMSlots = Column(Integer)
    Color = Column(String)
    Rating = Column(Integer)
    Price = Column(Integer)

class ramdata(Base):
    __tablename__ = 'ramdata'

    RAMID = Column(String, primary_key=True)
    RAMBrand = Column(String)
    RAMName = Column(String)
    Type = Column(String)
    Speed = Column(Integer)
    Modules = Column(String)
    TotalRAM = Column(Integer)
    Color = Column(String)
    FirstWordLatency = Column(String)
    CASLatency = Column(Integer)
    Rating = Column(Integer)
    PricePUnit = Column(Float)
    Price = Column(Integer)

cpuData = db.query(cpudata).all()
boardData = db.query(boarddata).all()
ramData = db.query(ramdata).all()

budget = int(input("Enter your Budget: "))
remainingBudgets = []
flag = 0
resultZero = []
resultNotZero = []

# for cpu in cpuData:
#     for board in boardData:
#         for ram in ramData:
#             expected = cpu.Price + board.Price + ram.Price
#             if expected == budget:
#                 expected = cpu.Price + board.Price + ram.Price
#                 resultZero.append([cpu.CPUID, board.BoardID, ram.RAMID])
#                 flag = 1
#                 break
#             else:
#                 if expected < budget:
#                     flag = 0
#                     remainingBudgets.append(budget - expected)
#                     resultNotZero.append([cpu.CPUID, board.BoardID, ram.RAMID, budget-expected])
#                     print(len(resultNotZero))


for cpu in cpuData:
    print(cpu.CPUID, cpu.CPUBrand)

