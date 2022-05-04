from random import choice

from logics.Admin.datashare import datatransfer

dataapi = datatransfer()


class logic:
    def autobuild(self, budget):
        new = []
        board = dataapi.getBOARDs(list=True)
        hdd = dataapi.getSTORAGEs(list=True)
        psu = dataapi.getPSUs(list=True)
        cabinet = dataapi.getCABINETs(list=True)
        pccounter = 0
        for counter in range(2000):
            try:
                brd = choice(board)
                cpu = dataapi.getCPUs(sockettype=brd[7], list=True)
                c = choice(cpu)
                ram = dataapi.getRAMs(ramtype=brd[11], list=True)
                rm = choice(ram)
                strg = choice(hdd)
                pu = choice(psu)
                cab = choice(cabinet)
                if c[-1] + brd[-1] + rm[-1] + strg[-1] + pu[-1] + cab[-1] <= budget:
                    new.append([c, brd, rm, strg, pu, cab, c[-1] + brd[-1] + rm[-1] + strg[-1] + pu[-1] + cab[-1]])
                    print('pc added')
                    pccounter += 1
                    if pccounter > 0:
                        break
            except:
                continue
        return new


if __name__ == '__main__':
    i = logic()
    n = i.autobuild(50000)
    for pcs in n:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        for pc in pcs:
            print(pc)
    print(len(n))
