# def biggie(newList):
#     for x in range(len(newList)):
#         if newList[x] > 0:
#             newList[x] = "big"
#     return newList

# def countP(newList):
#     count = 0
#     for val in newList:
#         if val > 0:
#             count += 1
#     newList[len(newList) - 1] = count
#     return newList

# print(countP([-1, 1, -2, 2, -3]))

# def sumT(newList):
#     total = 0
#     for val in newList:
#         total += val
#     return total

# print(sumT([3,5,8,7,9]))

# def ave(newList):
#     total = 0
#     for val in newList:
#         total += val
#     return float(total) / float(len(newList))

# print(ave([5,6,7,8,9,1]))

# def length(newList):
#     count = 0
#     for val in newList:
#         count += 1
#     return count

# print(length([1,3,5,4,8,9,5,1,]))

# def min(newList):
#     if len(newList) == 0:
#         return False
#     result = newList[0]
#     for val in newList:
#         if val < result:
#             result = val
#     return result

# print(min([1,6,8,7,9,8,3]))

# def max(newList):
#     if len(newList) == 0:
#         return False
#     result = newList[0]
#     for val in newList:
#         if val > result:
#             result = val
#     return result

# print(max([1,3,5,7,9,8,7]))

# def ultA(newList):
#     result = {
#         'sum': None,
#         'max': None,
#         'min': None,
#         'ave': None,
#         'length': 0
#     }
#     if len(newList) == 0:
#         return result
#     else:
#         result['sum'] = 0
#         result['max'] = newList[0]
#         result['min'] = newList[0]
#     for val in newList:
#         if val > result['max']:
#             result['max'] = val
#         elif val < result['min']:
#             result['min'] = val
#             result['sum'] += val
#             result['length'] += 1
#         result['ave'] = result['sum'] / len(newList)
#         return result

# print(ultA([1,5,7,9]))

def revList(newList):
    half = int(len(newList) / 2)
    for i in range(half):
        newList[i], newList[len(newList) - 1 - i] = newList[len(newList) - 1 - i], newList[i]
    return newList

print(revList([1,2,3,4,5,6,7,8,9]))