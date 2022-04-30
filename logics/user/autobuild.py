from random import choice

from logics.Admin.datashare import datatransfer

dataapi = datatransfer()


class logic:
    def autobuild(self, budget):
        new = []
        board = dataapi.getBOARDs(True)
        hdd = dataapi.getSTORAGEs(True)
        psu = dataapi.getPSUs(True)
        cabinet = dataapi.getCABINETs(True)
        for counter in range(1000):
            try:
                brd = choice(board)
                cpu = dataapi.getCPUs(brd[7], True)
                c = choice(cpu)
                ram = dataapi.getRAMs(brd[11], True)
                rm = choice(ram)
                strg = choice(hdd)
                pu = choice(psu)
                cab = choice(cabinet)
                if c[-1] + brd[-1] + rm[-1] + strg[-1] + pu[-1] + cab[-1] <= budget:
                    new.append([cpu, board, ram, hdd, psu, cabinet])
                    print('pc added')
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
