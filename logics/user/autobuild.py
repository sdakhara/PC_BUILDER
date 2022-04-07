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
    price = Column(Integer)
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
    price = Column(Integer)
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
    price = Column(Integer)
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
    price = Column(Integer)
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
    price = Column(Integer)
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
    price = Column(Integer)
    Type = Column(String)
    Color = Column(String)
    PowerSupply = Column(String)
    SidePanelWindow = Column(String)
    externalbays = Column(Integer)
    internalbays = Column(Integer)
    Rating = Column(Integer)

class coolerdata(Base):
    __tablename__ = 'coolerdata'
    collerID = Column(Integer, primary_key=True)
    collerName = Column(String)
    collerScore = Column(Float)
    price = Column(Integer)
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
    price = Column(Integer)
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
        coolerData = db.query(coolerdata).all()
        powersupplyData = db.query(powersupplydata).all()
        if not GPUneed:
            for cpu in cpuData:
                for motherboard in boardData:
                    for ram in ramData:
                        for hdd in hddData:
                            for cabinet in cabinetData:
                                for cooler in coolerData:
                                    for powersupply in powersupplyData:
                                        expected = cpu.price + motherboard.price + ram.price + hdd.price + cabinet.price + cooler.price + powersupply.price
                                        if expected == budget:
                                            expected = cpu.price + motherboard.price + ram.price + hdd.price + cabinet.price + cooler.price + powersupply.price
                                            # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                                            resultZero.append([cpu.cpuID, motherboard.boardID, ram.ramID, hdd.hddID, cabinet.cabinetID, cooler.cpllarID, powersupply.powersupplyID])
                                            break
                                        else:
                                            if (expected < budget):
                                                tempRemainBudget = budget-expected
                                                remainingBudgets.append(tempRemainBudget)
                                                cpulist = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.price, cpu.corecount, cpu.clockspeed, cpu.boostclock, cpu.sockettype, cpu.tdp, cpu.integretedgraphics, cpu.smt, cpu.rating]
                                                boardlist = [motherboard.boardID, motherboard.boardName, motherboard.boardScore, motherboard.price, motherboard.sockettype, motherboard.formfactor, motherboard.ramtype, motherboard.maxram, motherboard.ramslote, motherboard.color, motherboard.rating]
                                                ramlist = [ram.ramID, ram.ramName, ram.ramScore, ram.price, ram.speed, ram.module, ram.pricepergb, ram.color, ram.firstwordlatency, ram.caslatency, ram.rating]
                                                hddlist = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.price, hdd.capacity, hdd.pricepergb, hdd.type, hdd.cache, hdd.formfactor, hdd.interface, hdd.rating]
                                                cabinetlist = [cabinet.cabinetID, cabinet.cabinetName, cabinet.cabinetScore, cabinet.price, cabinet.type, cabinet.color, cabinet.powersupply, cabinet.sidepanelwindow, cabinet.externalbays, cabinet.internalbays, cabinet.rating]
                                                collerlist = [cooler.collerID, cooler.collerName, cooler.collerScore, cooler.price, cooler.fanRPM, cooler.noiselevel, cooler.color, cooler.radiotorsize, cooler.rating]
                                                powersupplylist = [powersupply.smpsID, powersupply.smpsName, powersupply.smpsScore, powersupply.price, powersupply.formfactor, powersupply.efficiencyrating, powersupply.wattage, powersupply.modular, powersupply.color, powersupply.rating]
                                                remainingBudget = [tempRemainBudget]
                                                resultNotZero.append([cpulist, boardlist, ramlist, hddlist, cabinetlist, collerlist, powersupplylist ,remainingBudget])

        if GPUneed:
            for cpu in cpuData:
                for motherboard in boardData:
                    for ram in ramData:
                        for hdd in hddData:
                            for gpu in gpuData:
                                for cabinet in cabinetData:
                                    for cooler in coolerData:
                                        for powersupply in powersupplyData:
                                            expected = cpu.price + motherboard.price + ram.price + hdd.price + gpu.price + cabinet.price + cooler.price + powersupply.price
                                            if expected == budget:
                                                expected = cpu.price + motherboard.price + ram.price + hdd.price + gpu.price + cabinet.price + cooler.price + powersupply.price
                                                # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                                                resultZero.append([cpu.cpuID, motherboard.boardID, ram.ramID, hdd.hddID, gpu.gpuID, cabinet.cabinetID, cooler.cpllarID, powersupply.powersupplyID])
                                                break
                                            else:
                                                if (expected < budget):
                                                    tempRemainBudget = budget-expected
                                                    remainingBudgets.append(tempRemainBudget)
                                                    cpulist = [cpu.cpuID, cpu.cpuName, cpu.cpuScore, cpu.price, cpu.corecount, cpu.clockspeed, cpu.boostclock, cpu.sockettype, cpu.tdp, cpu.integretedgraphics, cpu.smt, cpu.rating]
                                                    boardlist = [motherboard.boardID, motherboard.boardName, motherboard.boardScore, motherboard.price, motherboard.sockettype, motherboard.formfactor, motherboard.ramtype, motherboard.maxram, motherboard.ramslote, motherboard.color, motherboard.rating]
                                                    ramlist = [ram.ramID, ram.ramName, ram.ramScore, ram.price, ram.speed, ram.module, ram.pricepergb, ram.color, ram.firstwordlatency, ram.caslatency, ram.rating]
                                                    hddlist = [hdd.hddID, hdd.hddName, hdd.hddScore, hdd.price, hdd.capacity, hdd.pricepergb, hdd.type, hdd.cache, hdd.formfactor, hdd.interface, hdd.rating]
                                                    gpulist = [gpu.gpuID, gpu.gpuName, gpu.gpuScore, gpu.price, gpu.chipset, gpu.memory, gpu.coreclock, gpu.boostslock, gpu.color, gpu.lenght, gpu.rating]
                                                    cabinetlist = [cabinet.cabinetID, cabinet.cabinetName, cabinet.cabinetScore, cabinet.price, cabinet.type, cabinet.color, cabinet.powersupply, cabinet.sidepanelwindow, cabinet.externalbays,cabinet.internalbays, cabinet.rating]
                                                    collerlist = [cooler.collerID, cooler.collerName, cooler.collerScore, cooler.price, cooler.fanRPM, cooler.noiselevel, cooler.color, cooler.radiotorsize, cooler.rating]
                                                    powersupplylist = [powersupply.smpsID, powersupply.smpsName,powersupply.smpsScore, powersupply.price, powersupply.formfactor, powersupply.efficiencyrating, powersupply.wattage, powersupply.modular, powersupply.color, powersupply.rating]
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