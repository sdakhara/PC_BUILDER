from logics.Admin.datashare import datatransfer

dataapi = datatransfer()

class logic:
    def autobuild(self, budget):
        new = []
        for cpu in dataapi.getCPUs(True):
            tempBudget = budget
            tempBudget -= cpu[-1]
            budoncpu = tempBudget
            for board in dataapi.getBOARDs(cpu[13], True):
                if board[-1] > budoncpu:
                    continue
                else:
                    tempBudget -= board[-1]
                    budonboard = tempBudget
                for ram in dataapi.getRAMs(board[11], True):
                    if ram[-1] > budonboard:
                        continue
                    else:
                        tempBudget -= ram[-1]
                        budonram = tempBudget
                    for hdd in dataapi.getSTORAGEs(True):
                        if hdd[-1] > budonram:
                            continue
                        else:
                            tempBudget -= hdd[-1]
                            budonstorage = tempBudget
                        for psu in dataapi.getPSUs(True):
                            if psu[-1] > budonstorage:
                                continue
                            else:
                                tempBudget -= psu[-1]
                                budonpsu = tempBudget
                            for cabinet in dataapi.getCABINETs(True):
                                if cabinet[-1] > budonpsu:
                                    continue
                                else:
                                    tempBudget -= cabinet[-1]
                                if cpu[-1]+board[-1]+ram[-1]+hdd[-1]+psu[-1]+cabinet[-1] < budget:
                                    new.append([cpu, board, ram, hdd, psu, cabinet,[cpu[-1]+board[-1]+ram[-1]+hdd[-1]+psu[-1]+cabinet[-1]]])
                                    print('pc added')
                                    break

        new.reverse()
        return new

if __name__ == '__main__':
    i = logic()
    n = i.autobuild(50000)
    for pcs in n:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for pc in pcs:
            print(pc)
    print(len(n))
