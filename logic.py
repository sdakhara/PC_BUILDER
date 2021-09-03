# data = 10000
# cpus = [5000, 9000, 20000]
# motherboards = [2000, 2500, 3500]
# for cpu in cpus:
#     for motherboard in motherboards:
#         if ((cpu+motherboard)==data):
#             print(cpu, motherboard)
#         else:
#             if((cpu+motherboard)<data):
#                 print(cpu, motherboard, data-(cpu+motherboard))

budget = int(input("Enter Your Budget: "))
cpus = [5000, 7500, 10000]
motherboards = [2000, 3000, 3500]
rams = [1000, 3500, 4000]
hdds = [1000, 3000, 5000]
cabinets = [1000, 1500, 5000]
remainingBudget = []
flag = 0
resultZero = []
resultNotZero = []
for cpu in cpus:
    for motherboard in motherboards:
        for ram in rams:
            for hdd in hdds:
                for cabinet in cabinets:
                    expected = cpu+motherboard+ram+hdd+cabinet
                    if expected == budget:
                        expected = cpu+motherboard+ram+hdd+cabinet
                        # print(cpu, motherboard, ram, hdd, cabinet,"this is 0")
                        resultZero.append([cpu, motherboard, ram, hdd, cabinet])
                        
                        flag = 1
                        break
                    else:
                        if (expected<budget):
                            flag = 0
                            remainingBudget.append(budget-expected)
                            # print(cpu, motherboard, ram, hdd, cabinet, budget-expected)
                            resultNotZero.append([cpu, motherboard, ram, hdd, cabinet, budget-expected])
print("------------------------------------------------THIS IS RESULT ZERO PC------------------------------------------------")
for result in resultZero:
    print(result)
print("------------------------------------------------THIS IS RESULT NOT ZERO PC------------------------------------")
for result in resultNotZero:
    print(result)
