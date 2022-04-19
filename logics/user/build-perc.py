# with GPU


def my_function():
    total = 68314

    cpu = (total * 15) / 100
    print(int(cpu))

    board = (total * 15) / 100
    print(int(board))

    gpu = (total * 20) / 100
    print(int(gpu))

    ram = (total * 15) / 100
    print(int(ram))

    psu = (total * 10) / 100
    print(int(psu))

    cabinet = (total * 7) / 100
    print(int(cabinet))

    cooler = (total * 8) / 100
    print(int(cooler))
    storage = (total * 10) / 100
    print(int(storage))
    print(cpu + board + gpu + ram + psu + cabinet + cooler + storage)


my_function()


# without GPU


def my_function():
    total = 68314

    cpu = (total * 25) / 100
    print(int(cpu))

    board = (total * 20) / 100
    print(int(board))

    gpu = (total * 5) / 100
    print(int(gpu))

    ram = (total * 15) / 100
    print(int(ram))

    psu = (total * 10) / 100
    print(int(psu))

    cabinet = (total * 10) / 100
    print(int(cabinet))

    cooler = (total * 5) / 100
    print(int(cooler))

    storage = (total * 10) / 100
    print(int(storage))
    print(cpu + board + gpu + ram + psu + cabinet + cooler + storage)


my_function()