
# 1. Retuens the pc with the highest score of one pc
# 2. Retuens the PC with highest score in CPU only
# 3. Returns the PC with highest score in RAM only
# 4. Returns the PC with the highest score in HDD only

# total 3 needs ram and cpu=1, cpu and hdd=2, hdd and ram=3
def multipleneed(leastpclist, needs=0):
    if needs == 0:
        pcwithfilter(leastpclist)
    if needs == 1:
        pass
    if needs == 2:
        pass
    if needs == 3:
        pass

# returns the pc with the filters
def pcwithfilter(leastpclist, cpuneed=False, ramneed=False, hddneed=False):
    counter = 0
    onescore = 0
    highestscore = 0
    finalpc = []
    for pc in leastpclist:
        for component in pc:
            if counter < 4:
                # print(component)
                if not cpuneed and not ramneed and not hddneed:
                    onescore += component[2]
                    # print(component)
                elif cpuneed:
                    if counter == 0:
                        onescore = component[2]
                elif ramneed:
                    if counter == 2:
                        onescore = component[2]
                elif hddneed:
                    if counter == 3:
                        onescore = component[2]
                elif cpuneed and ramneed:
                    if counter == 0 or counter == 2:
                        onescore += component[2]
                elif cpuneed and hddneed:
                    if counter == 0 or counter == 4:
                        onescore += component[2]
                elif hddneed and ramneed:
                    if counter == 2 or counter == 4:
                        onescore += component[2]
                elif cpuneed and ramneed and hddneed:
                    if counter == 0 or counter == 2 or counter == 4:
                        onescore += component[2]
                counter += 1
            elif counter == 4:
                if highestscore <= onescore:
                    highestscore = onescore
                    finalpc.append(pc)
                    onescore = 0
                else:
                    onescore = 0
                counter = 0

    return finalpc
