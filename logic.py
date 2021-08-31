number = [20, 30, 40]
a = 50
result = []
# print(max(number))
# def algo():
#     if (max(number)<=a):
#         result.append(max(number))
#         a = a - max(number)
#         print(a)
#         print(result)
#     else:
#         algo()    
        
def algo(data, high):
    result =[]
    if (high!=0):
        if (max(data)<=high):
            result.append(max(data))
            high = high - max(data)
            print(high)
            print(result)
        else:
            algo()
            
