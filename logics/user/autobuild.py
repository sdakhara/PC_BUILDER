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
        remainingBudgets = []
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
                                tempRemainBudget = budget-expected
                                remainingBudgets.append(tempRemainBudget)
                                cpulist = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.Price]
                                boardlist = [motherboard.boardID, motherboard.boardName, motherboard.boardScore,
                                             motherboard.Price]
                                ramlist = [ram.ramID, ram.ramName, ram.ramScore, ram.Price]
                                hddlist = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.Price]
                                remainingBudget = [tempRemainBudget]
                                resultNotZero.append([cpulist, boardlist, ramlist, hddlist, remainingBudget])
        remainingBudgets.sort()
        least = []
        for result in resultNotZero:
            if result[-1][0] == remainingBudgets[0]:
                least.append(result)
        counter = 0
        onePCScore = 0
        highestRecordedScore = 0
        highScorePC = []
        for pc in least:
            for component in pc:
                if counter < 4:
                    onePCScore += component[2]
                    counter += 1
                elif counter == 4:
                    if highestRecordedScore <= onePCScore:
                        highestRecordedScore = onePCScore
                        highScorePC.append(pc)
                        highScorePC.append(onePCScore)
                        onePCScore = 0
                    else:
                        onePCScore = 0
                    counter = 0
        return highScorePC
