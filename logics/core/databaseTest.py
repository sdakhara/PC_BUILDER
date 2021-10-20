from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer, Float, String
from logics.user.autobuildfunctions import *


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


def printer(a):
    counter = 1
    for data in a:
        if counter == 1:
            print(f"""
            -------------------------
            CPU ID: {data[0]}
            CPU Name: {data[1]}
            CPU Score: {data[2]}
            CPU Price: {data[3]}
            """)
            counter += 1
        elif counter == 2:
            print(f"""
            Motherboard ID: {data[0]}
            Motherboard Name: {data[1]}
            Motherboard Score: {data[2]}
            Motherboard Price: {data[3]}
            """)
            counter += 1
        elif counter == 3:
            print(f"""
            RAM ID: {data[0]}
            RAM Name: {data[1]}
            RAM Score: {data[2]}
            RAM Price: {data[3]}
            """)
            counter += 1
        elif counter == 4:
            print(f"""
            HDD ID: {data[0]}
            HDD Name: {data[1]}
            HDD Score: {data[2]}
            HDD Price: {data[3]}
            """)
            counter += 1
        elif counter == 5:
            print(f"""
            Remaining Budget: {data[0]}
            """)
            counter = 1






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
                    if expected < budget:
                        flag = 0
                        remainingBudgets.append(budget - expected)
                        # print(cpu, motherboard, ram, hdd, cabinet, budget-expected)
                        cpuList = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.Price]
                        boardList = [motherboard.boardID, motherboard.boardName, motherboard.boardScore, motherboard.Price]
                        ramList = [ram.ramID, ram.ramName, ram.ramScore, ram.Price]
                        hddList = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.Price]
                        remainingBudget = [budget-expected]
                        resultNotZero.append([cpuList, boardList, ramList, hddList, remainingBudget])

remainingBudgets.sort()
least = []
for result in resultNotZero:
    if result[-1][0] == remainingBudgets[0]:
        least.append(result)
# for result in least:
#     printer(result)
print(pcwithfilter(least,cpuneed=True, hddneed=True))

