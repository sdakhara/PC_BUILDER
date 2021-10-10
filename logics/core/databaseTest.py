from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, Float, String


engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/logictest")
Session = sessionmaker()
db = Session(bind=engine)
Base = declarative_base()


class cpudata(Base):
    __tablename__ = 'cpudata'

    cpuID = Column(Integer, primary_key=True)
    cpuName = Column(String)
    cpuScore = Column(Float)
    Price = Column(Integer)


class boarddata(Base):
    __tablename__ = 'boarddata'

    boardID = Column(Integer, primary_key=True)
    boardName = Column(String)
    boardScore = Column(Float)
    Price = Column(Integer)


class ramdata(Base):
    __tablename__ = 'ramdata'

    ramID = Column(Integer, primary_key=True)
    ramName = Column(String)
    ramScore = Column(Float)
    Price = Column(Integer)


class hdddata(Base):
    __tablename__ = 'hdddata'
    hddID = Column(Integer, primary_key=True)
    hddName = Column(String)
    hddScore = Column(Float)
    Price = Column(Integer)




cpuData = db.query(cpudata).all()
boardData = db.query(boarddata).all()
ramData = db.query(ramdata).all()
hddData = db.query(hdddata).all()
budget = int(input("Enter your Budget: "))
remainingBudgets = []
flag = 0
resultZero = []
resultNotZero = []
for cpu in cpuData:
    for motherboard in boardData:
        for ram in ramData:
            for hdd in hddData:
                expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price
                if expected == budget:
                    expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price
                    # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                    resultZero.append([cpu.cpuID, motherboard.boardID, ram.ramID, hdd.hddID])
                    flag = 1
                    break
                else:
                    if (expected < budget):
                        flag = 0
                        remainingBudgets.append(budget - expected)
                        # print(cpu, motherboard, ram, hdd, cabinet, budget-expected)
                        cpuList = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.Price]
                        boardList = [motherboard.boardID, motherboard.boardName, motherboard.boardScore, motherboard.Price]
                        ramList = [ram.ramID, ram.ramName, ram.ramScore, ram.Price]
                        hddList = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.Price]
                        remainingBudget = budget - expected
                        resultNotZero.append([cpuList, boardList, ramList, hddList, remainingBudget])

print(resultNotZero[1])
remainingBudgets.sort()
least = []
for result in resultNotZero:
    if result[-1] == remainingBudgets[1]:
        least.append(result)
for result in least:
    print(result)

