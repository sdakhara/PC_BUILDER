def srt(e):
    return e[-1]


def sortcpu(cpuobj):
    cpuData = []
    for cpu in cpuobj:
        cpulist = ["CPU", cpu.CPUID,
                   "CPU Brand", cpu.CPUBrand,
                   "CPU Name", cpu.CPUName,
                   "Core Count", cpu.CoreCount,
                   "Clock Speed", cpu.ClockSpeed,
                   "Boost Clock", cpu.BoostClock,
                   "Socket Type", cpu.SocketType,
                   "TDP", cpu.TDP,
                   "Integrated Graphics ", cpu.IntegratedGraphics,
                   "SMT", cpu.SMT,
                   "Rating", cpu.Rating,
                   "Price", cpu.Price
                   ]
        cpuData.append(cpulist)
    cpuData.sort(key=srt)
    return cpuData


def sortgpu(gpuobj):
    gpuData = []
    for gpu in gpuobj:
        gpulist = ["GPU", gpu.GPUID,
                   "GPU Brand", gpu.GPUBrand,
                   "GPU Name", gpu.GPUName,
                   "Chipset", gpu.Chipset,
                   "Memory", gpu.Memory,
                   "Core Clock", gpu.CoreClock,
                   "Boost Clock", gpu.BoostClock,
                   "Color", gpu.Color,
                   "Length", gpu.Length,
                   "Rating", gpu.Rating,
                   "Price", gpu.Price
                   ]
        gpuData.append(gpulist)
    gpuData.sort(key=srt)
    return gpuData


def sortram(ramobj):
    ramData = []
    for ram in ramobj:
        ramlist = ["RAM", ram.RAMID,
                   "RAM Brand", ram.RAMBrand,
                   "RAM Name", ram.RAMName,
                   "Type", ram.Type,
                   "Speed", ram.Speed,
                   "Modules", ram.Modules,
                   "Price Per Module", ram.PricePerModule,
                   "Size Per Module", ram.SizePerModule,
                   "Color", ram.Color,
                   "First Word Latency", ram.FirstWordLatency,
                   "CAS Latency", ram.CASLatency,
                   "Rating", ram.Rating,
                   "Price", ram.Price
                   ]
        ramData.append(ramlist)
    ramData.sort(key=srt)
    return ramData


def sortboard(boardobj):
    boardData = []
    for board in boardobj:
        boardlist = ["Board", board.BoardID,
                     "Board Brand", board.BoardBrand,
                     "Board Name", board.BoardName,
                     "Socket Type", board.SocketType,
                     "Form Factor", board.FormFactor,
                     "RAM Type", board.RAMType,
                     "Max Ram", board.MaxRam,
                     "RAM Slots", board.RAMSlots,
                     "Color", board.Color,
                     "Rating", board.Rating,
                     "Price", board.Price
                     ]
        boardData.append(boardlist)
    boardData.sort(key=srt)
    return boardData


def sortcooler(coolerobj):
    coolerData = []
    for cooler in coolerobj:
        coolerlist = ["Cooler", cooler.CoolerID,
                      "Cooler Brand", cooler.CoolerBrand,
                      "Cooler Name", cooler.CoolerName,
                      "Fan RPM", cooler.FanRPM,
                      "Noise Level", cooler.NoiseLevel,
                      "Color", cooler.Color,
                      "Radiator Size", cooler.RadiatorSize,
                      "Rating", cooler.Rating,
                      "Price", cooler.Price]
        coolerData.append(coolerlist)
    coolerData.sort(key=srt)
    return coolerData


def sorthdd(hddobj):
    hddData = []
    for storage in hddobj:
        storagelist = ["Storage", storage.StorageID,
                       "Storage Brand", storage.StorageBrand,
                       "Storage Name", storage.StorageName,
                       "Capacity", storage.Capacity,
                       "Type", storage.Type,
                       "Cache", storage.Cache,
                       "Form Factor", storage.FormFactor,
                       "Interface", storage.Interface,
                       "Rating", storage.Rating,
                       "Price", storage.Price
                       ]
        hddData.append(storagelist)
    hddData.sort(key=srt)
    return hddData


def sortcabinet(cabobj):
    cabData = []
    for cabinet in cabobj:
        cabinetlist = ["Cabinet", cabinet.CabinetID,
                       "Cabinet Brand", cabinet.CabinetBrand,
                       "Cabinet Name", cabinet.CabinetName,
                       "Type", cabinet.Type,
                       "Color", cabinet.Color,
                       "Power Supply", cabinet.PowerSupply,
                       "Side Panel Window", cabinet.SidePanelWindow,
                       "External Bays", cabinet.ExternalBays,
                       "Internal Bays", cabinet.InternalBays,
                       "Rating", cabinet.Rating,
                       "Price", cabinet.Price
                       ]
        cabData.append(cabinetlist)
    cabData.sort(key=srt)
    return cabData


def sortpsu(psuobj):
    psuData = []
    for psu in psuobj:
        powersupplylist = ["Smps", psu.SmpsID,
                           "Smps Brand", psu.SmpsBrand,
                           "Smps Name", psu.SmpsName,
                           "Form Factor", psu.FormFactor,
                           "Efficiency Rating", psu.EfficiencyRating,
                           "Wattage", psu.Wattage,
                           "Modular", psu.Modular,
                           "Color", psu.Color,
                           "Rating", psu.Rating,
                           "Price", psu.Price
                           ]
        psuData.append(powersupplylist)
    psuData.sort(key=srt)
    return psuData
