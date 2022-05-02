from random import choice

from logics.Admin.datashare import datatransfer

dataapi = datatransfer()


class logic:
    def autobuild(self, budget):
        new = []
        board = dataapi.getBOARDs()
        hdd = dataapi.getSTORAGEs()
        psu = dataapi.getPSUs()
        cabinet = dataapi.getCABINETs()
        for counter in range(1000):
            try:
                brd = choice(board)
                cpu = dataapi.getCPUs(sockettype=brd[7], list=True)
                c = choice(cpu)
                ram = dataapi.getRAMs(brd[11], list=True)
                rm = choice(ram)
                strg = choice(hdd)
                pu = choice(psu)
                cab = choice(cabinet)
                if c[-1] + brd[-1] + rm[-1] + strg[-1] + pu[-1] + cab[-1] <= budget:
                    new.append([c, brd, rm, strg, pu, cab])
                    print('pc added')
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
