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
    corecount = Column(Integer)
    clockspeed = Column(String)
    boostclock = Column(String)
    sockettype = Column(String)
    tdp = Column(String)
    integretedgraphics = Column(String)
    smt = Column(String)
    rating = Column(Integer)

class gpudata(Base):
    __tablename__ = 'gpudata'

    gpuID = Column(Integer, primary_key=True)
    gpuName = Column(String)
    gpuScore = Column(Float)
    Price = Column(Integer)
    chipset = Column(String)
    memory = Column(String)
    coreclock = Column(String)
    boostclock = Column(String)
    color = Column(String)
    lenght = Column(Integer)
    rating = Column(Integer)



class boarddata(Base):
    __tablename__ = 'boarddata'

    boardID = Column(Integer, primary_key=True)
    boardName = Column(String)
    boardScore = Column(Float)
    Price = Column(Integer)
    SocketType = Column(String)
    FormFactor = Column(String)
    RAMType = Column(String)
    MaxRam = Column(String)
    RAMSlots = Column(String)
    Color = Column(String)
    Rating = Column(Integer)


class ramdata(Base):
    __tablename__ = 'ramdata'

    ramID = Column(Integer, primary_key=True)
    ramName = Column(String)
    ramScore = Column(Float)
    Price = Column(Integer)
    speed = Column(String)
    modules = Column(String)
    pricepergb = Column(String)
    color = Column(String)
    firstwordlatency = Column(String)
    caslatency = Column(String)
    rating = Column(Integer)


class hdddata(Base):
    __tablename__ = 'hdddata'
    hddID = Column(Integer, primary_key=True)
    hddName = Column(String)
    hddScore = Column(Float)
    Price = Column(Integer)
    capacity = Column(String)
    pricepergb = Column(String)
    type = Column(String)
    cache = Column(String)
    formfactor = Column(String)
    interface = Column(String)
    rating = Column(Integer)


class cabinetdata(Base):
    __tablename__ = 'cabinetdata'
    cabinetID = Column(Integer, primary_key=True)
    cabinetName = Column(String)
    cabinetScore = Column(Float)
    Price = Column(Integer)
    Type = Column(String)
    Color = Column(String)
    PowerSupply = Column(String)
    SidePanelWindow = Column(String)
    externalbays = Column(Integer)
    internalbays = Column(Integer)
    Rating = Column(Integer)

class collerdata(Base):
    __tablename__ = 'collerdata'
    collerID = Column(Integer, primary_key=True)
    collerName = Column(String)
    collerScore = Column(Float)
    Price = Column(Integer)
    fanRPM = Column(String)
    noiselevel = Column(String)
    color = Column(String)
    radiotorsize = Column(String)
    rating = Column(Integer)


class powersupplydata(Base):
    __tablename__ = 'powersupplydata'
    smpsID = Column(Integer, primary_key=True)
    smpsName = Column(String)
    smpsScore = Column(Float)
    Price = Column(Integer)
    formfactor = Column(String)
    efficiencyrating = Column(String)
    wattage = Column(String)
    modular = Column(String)
    color = Column(String)
    rating = Column(Integer)








class logic:
    def buildpc(self, budget, CPUneed = False, RAMneed = False, HDDneed = False, GPUneed = False,):
        remainingBudgets = []
        resultZero = []
        resultNotZero = []
        cpuData = db.query(cpudata).all()
        boardData = db.query(boarddata).all()
        gpuData = db.query(gpudata).all()
        ramData = db.query(ramdata).all()
        hddData = db.query(hdddata).all()
        cabinetData = db.query(cabinetdata).all()
        collerData = db.query(collerdata).all()
        powersupplyData = db.query(powersupplydata).all()
        if not GPUneed:
            for cpu in cpuData:
                for motherboard in boardData:
                    for ram in ramData:
                        for hdd in hddData:
                            for cabinet in cabinetData:
                                for coller in collerData:
                                    for powersupply in powersupplyData:
                                        expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price + cabinet.Price + coller.Price + powersupply.Price
                                        if expected == budget:
                                            expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price + cabinet.Price + coller.Price + powersupply.Price
                                            # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                                            resultZero.append([cpu.cpuID, motherboard.boardID, ram.ramID, hdd.hddID, cabinet.cabinetID, coller.cpllarID, powersupply.powersupplyID])
                                            break
                                        else:
                                            if (expected < budget):
                                                tempRemainBudget = budget-expected
                                                remainingBudgets.append(tempRemainBudget)
                                                cpulist = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.Price]
                                                boardlist = [motherboard.boardID, motherboard.boardName, motherboard.boardScore, motherboard.Price]
                                                ramlist = [ram.ramID, ram.ramName, ram.ramScore, ram.Price]
                                                hddlist = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.Price]
                                                cabinetlist = [cabinet.cabinetID, cabinet.cabinetName, cabinet.cabinetScore, cabinet.Price]
                                                collerlist = [coller.collerID, coller.collerName, coller.collerScore, coller.Price]
                                                powersupplylist = [powersupply.powersupplyID, powersupply.powersupplyName, powersupply.powersupplyScore, powersupply.Price]
                                                remainingBudget = [tempRemainBudget]
                                                resultNotZero.append([cpulist, boardlist, ramlist, hddlist, cabinetlist, collerlist, powersupplylist ,remainingBudget])
        if GPUneed:
            for cpu in cpuData:
                for motherboard in boardData:
                    for ram in ramData:
                        for hdd in hddData:
                            for gpu in gpuData:
                                for cabinet in cabinetData:
                                    for coller in collerData:
                                        for powersupply in powersupplyData:
                                            expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price + gpu.Price + cabinet.Price + coller.Price + powersupply.Price
                                            if expected == budget:
                                                expected = cpu.Price + motherboard.Price + ram.Price + hdd.Price + gpu.Price + cabinet.Price + coller.Price + powersupply.Price
                                                # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                                                resultZero.append([cpu.cpuID, motherboard.boardID, ram.ramID, hdd.hddID, gpu.gpuIDcabinet.cabinetID, coller.cpllarID, powersupply.powersupplyID])
                                                break
                                            else:
                                                if (expected < budget):
                                                    tempRemainBudget = budget-expected
                                                    remainingBudgets.append(tempRemainBudget)
                                                    cpulist = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.Price]
                                                    boardlist = [motherboard.boardID, motherboard.boardName, motherboard.boardScore, motherboard.Price]
                                                    ramlist = [ram.ramID, ram.ramName, ram.ramScore, ram.Price]
                                                    hddlist = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.Price]
                                                    gpulist = [gpu.gpuID, gpu.gpuName, gpu.gpuScore, gpu.Price]
                                                    cabinetlist = [cabinet.cabinetID, cabinet.cabinetName, cabinet.cabinetScore, cabinet.Price]
                                                    collerlist = [coller.collerID, coller.collerName, coller.collerScore, coller.Price]
                                                    powersupplylist = [powersupply.powersupplyID, powersupply.powersupplyName,powersupply.powersupplyScore, powersupply.Price]
                                                    remainingBudget = [tempRemainBudget]
                                                    resultNotZero.append([cpulist, boardlist, ramlist, hddlist, gpulist, cabinetlist, collerlist, powersupplylist, remainingBudget])
        remainingBudgets.sort()
        least = []
        for result in resultNotZero:
            if result[-1][0] == remainingBudgets[0]:
                least.append(result)
        return pcwithfilter(least, CPUneed, RAMneed, HDDneed, GPUneed)
        # return highestscorepc(least)
        # return least