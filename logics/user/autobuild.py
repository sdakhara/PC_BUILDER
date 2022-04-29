from logics.Admin.datashare import datatransfer

dataapi = datatransfer()
cpus = dataapi.getCPUs(True)
# boards = dataapi.getBOARDs(True)
hdds = dataapi.getSTORAGEs(True)
# rams = dataapi.getRAMs(True)
gpus = dataapi.getGPUs(True)


class logic:
    def autobuild(self, budget):
        new = []
        for cpu in dataapi.getCPUs(True):
            tempBudget = budget
            tempBudget -= cpu[-1]
            for board in dataapi.getBOARDs(cpu[6], True):
                if board[-1] > tempBudget:
                    continue
                else:
                    tempBudget -= board[-1]
                for ram in dataapi.getRAMs(board[5], True):
                    if ram[-1] > tempBudget:
                        continue
                    else:
                        tempBudget -= ram[-1]
                    for hdd in dataapi.getSTORAGEs(True):
                        if hdd[-1] > tempBudget:
                            continue
                        else:
                            tempBudget -= hdd[-1]
                        for psu in dataapi.getPSUs(True):
                            if psu[-1] > tempBudget:
                                continue
                            else:
                                tempBudget -= psu[-1]
                            for cabinet in dataapi.getCABINETs(True):
                                if cabinet[-1] > tempBudget:
                                    continue
                                else:
                                    tempBudget -= cabinet[-1]
                                if cpu[-1]+board[-1]+ram[-1]+hdd[-1]+psu[-1]+cabinet[-1] < budget:
                                    new.append([cpu, board, ram, hdd, psu, cabinet,cpu[-1]+board[-1]+ram[-1]+hdd[-1]+psu[-1]+cabinet[-1]])
                                    print('pc added')
                                    break
        return new

if __name__ == '__main__':
    i = logic()
    n = i.autobuild(50000)
    for pcs in n:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for pc in pcs:
            print(pc)
    print(len(n))
