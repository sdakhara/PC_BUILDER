from logics.admin.datashare import datatransfer

dataapi = datatransfer()
cpus = dataapi.getCPUs(True)
boards = dataapi.getBOARDs(True)
hdds = dataapi.getSTORAGEs(True)
rams = dataapi.getRAMs(True)
gpus = dataapi.getGPUs(True)


class logic:
    def autobuild(self, budget):
        new = []
        expected = None
        for cpu in cpus:
            expected = cpu[-1]
            print('1')
            if cpu[-1] > budget or cpu[-1] > expected:
                continue
            for board in boards:
                expected = cpu[-1] + board[-1]
                print('2')
                if board[-1] > budget or board[-1] > expected:
                    continue
                for hdd in hdds:
                    print('3')
                    expected = cpu[-1] + board[-1] + hdd[-1]
                    if hdd[-1] > budget or hdd[-1] > expected:
                        continue
                    for ram in rams:
                        expected = cpu[-1] + board[-1] + hdd[-1] + ram[-1]
                        print('4')
                        if ram[-1] > budget or ram[-1] > expected:
                            continue
                        for gpu in gpus:
                            expected = cpu[-1] + board[-1] + hdd[-1] + ram[-1] + gpu[-1]
                            print('5')
                            if ram[-1] > budget or ram[-1] > expected:
                                continue
                            if expected <= budget:
                                new.append([cpu, board, hdd, ram, gpu])
        return new

i = logic()
n = i.autobuild(8000)
for pc in n:
    print('1')
    print(pc)
