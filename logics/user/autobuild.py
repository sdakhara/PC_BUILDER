from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Integer

engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/logictest")
Session = sessionmaker()
db = Session(bind=engine)
Base = declarative_base()


class cpudata(Base):
    __tablename__ = 'cpudata'
    cpuID = Column(Integer, primary_key=True)
    Price = Column(Integer)


class boarddata(Base):
    __tablename__ = 'boarddata'
    boardID = Column(Integer, primary_key=True)
    Price = Column(Integer)


class ramdata(Base):
    __tablename__ = 'ramdata'
    ramID = Column(Integer, primary_key=True)
    Price = Column(Integer)


class hdddata(Base):
    __tablename__ = 'hdddata'
    hddID = Column(Integer, primary_key=True)
    Price = Column(Integer)


def printer(a):
    print(f"""
    CPU ID: {a[0]}
    CPU Price: {a[1]}
    Board ID: {a[2]}
    Board Price: {a[3]}
    RAM ID: {a[4]}
    RAM Price: {a[5]}
    HDD ID: {a[6]}
    HDD Price: {a[7]}
    Remaining Budget: {a[8]}
--------------------------------
    """)


class logic:
    def buildpc(self, budget):
        remainingBudget = []
        resultZero = []
        resultNotZero = []
        cpuData = db.query(cpudata).all()
        boardData = db.query(boarddata).all()
        ramData = db.query(ramdata).all()
        hddData = db.query(hdddata).all()
        for cpu in cpuData:
            for motherboard in boardData:
                for ram in ramData:
                    for hdd in hddData:
                        expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price
                        if expected == budget:
                            expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price
                            # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                            resultZero.append([cpu.cpuID, motherboard.boardID, ram.ramID, hdd.hddID])
                            break
                        else:
                            if (expected < budget):
                                remainingBudget.append(budget - expected)
                                # print(cpu, motherboard, ram, hdd, cabinet, budget-expected)
                                resultNotZero.append(
                                    [cpu.cpuID, cpu.Price, motherboard.boardID, motherboard.Price, ram.ramID,
                                     ram.Price, hdd.hddID, hdd.Price, budget - expected])
        remainingBudget.sort()
        least = []
        for result in resultNotZero:
            if result[-1] == remainingBudget[1]:
                least.append(result)
        # for result in least:
            # printer(result)
        return least
