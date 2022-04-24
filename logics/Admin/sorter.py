def srt(e):
    return e[-1]


def sortcpu(cpuobj):
    cpuData = []
    for cpu in cpuobj:
        cpulist = [cpu.CPUID, cpu.CPUBrand, cpu.CPUName, cpu.CoreCount, cpu.ClockSpeed,
                   cpu.BoostClock, cpu.SocketType, cpu.TDP,
                   cpu.IntegratedGraphics, cpu.SMT, cpu.Rating, cpu.Price]
        cpuData.append(cpulist)
    cpuData.sort(key=srt)
    return cpuData


def sortgpu(gpuobj):
    gpuData = []
    for gpu in gpuobj:
        gpulist = [gpu.GPUID, gpu.GPUBrand, gpu.GPUName, gpu.Chipset, gpu.Memory,
                   gpu.CoreClock, gpu.BoostClock, gpu.Color, gpu.Length,
                   gpu.Rating, gpu.Price
                   ]
        gpuData.append(gpulist)
    gpuData.sort(key=srt)
    return gpuData


def sortram(ramobj):
    ramData = []
    for ram in ramobj:
        ramlist = [ram.RAMID, ram.RAMBrand, ram.RAMName, ram.Type, ram.Speed, ram.Modules,
                   ram.PricePerModule, ram.SizePerModule, ram.Color,
                   ram.FirstWordLatency, ram.CASLatency, ram.Rating, ram.Price
                   ]
        ramData.append(ramlist)
    ramData.sort(key=srt)
    return ramData


def sortboard(boardobj):
    boardData = []
    for board in boardobj:
        boardlist = [board.BoardID, board.BoardBrand, board.BoardName, board.SocketType,
                     board.FormFactor, board.RAMType, board.MaxRam,
                     board.RAMSlots, board.Color, board.Rating, board.Price]
        boardData.append(boardlist)
    boardData.sort(key=srt)
    return boardData


def sortcooler(coolerobj):
    coolerData = []
    for cooler in coolerobj:
        coolerlist = [cooler.CoolerID, cooler.CoolerBrand, cooler.CoolerName, cooler.FanRPM,
                      cooler.NoiseLevel, cooler.Color, cooler.RadiatorSize,
                      cooler.Rating, cooler.Price]
        coolerData.append(coolerlist)
    coolerData.sort(key=srt)
    return coolerData


def sorthdd(hddobj):
    hddData = []
    for storage in hddobj:
        storagelist = [storage.StorageID, storage.StorageBrand, storage.StorageName, storage.Capacity,
                       storage.Type, storage.Cache, storage.FormFactor,
                       storage.Interface, storage.Rating, storage.Price]
        hddData.append(storagelist)
    hddData.sort(key=srt)
    return hddData


def sortcabinet(cabobj):
    cabData = []
    for cabinet in cabobj:
        cabinetlist = [cabinet.CabinetID, cabinet.CabinetBrand, cabinet.CabinetName, cabinet.Type,
                       cabinet.Color, cabinet.PowerSupply,
                       cabinet.SidePanelWindow, cabinet.ExternalBays,
                       cabinet.InternalBays, cabinet.Rating, cabinet.Price
                       ]
        cabData.append(cabinetlist)
    cabData.sort(key=srt)
    return cabData


def sortpsu(psuobj):
    psuData = []
    for psu in psuobj:
        powersupplylist = [psu.SmpsID, psu.SmpsBrand, psu.SmpsName, psu.FormFactor,
                           psu.EfficiencyRating, psu.Wattage, psu.Modular,
                           psu.Color, psu.Rating, psu.Price
                           ]
        psuData.append(powersupplylist)
    psuData.sort(key=srt)
    return psuData
