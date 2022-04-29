from random import choice

from logics.admin.datashare import datatransfer

dataapi = datatransfer()


class logic:
    def autobuild(self, budget):
        new = []
        board = dataapi.getBOARDs(True)
        hdd = dataapi.getSTORAGEs(True)
        psu = dataapi.getPSUs(True)
        cabinet = dataapi.getCABINETs(True)
        for counter in range(1000):
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

        #
        # for cpu in dataapi.getCPUs(True):
        #     if counter > 100:
        #         continue
        #     for board in dataapi.getBOARDs(cpu[13], True):
        #         if counter > 100:
        #             continue
        #         for ram in dataapi.getRAMs(board[11], True):
        #             if counter > 100:
        #                 continue
        #             for hdd in dataapi.getSTORAGEs(True):
        #                 if counter > 100:
        #                     continue
        #                 for psu in dataapi.getPSUs(True):
        #                     if counter > 100:
        #                         continue
        #                     for cabinet in dataapi.getCABINETs(True):
        #                         if counter > 100:
        #                             continue
        #                         if cpu[-1] + board[-1] + ram[-1] + hdd[-1] + psu[-1] + cabinet[-1] <= budget:
        #                             new.append([cpu, board, ram, hdd, psu, cabinet])
        #                             print('pc added')
        #                             counter += 1
        #                             break

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
