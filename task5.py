src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 105, 6, 8, 7, 6, 89]
res = {}
for ls in src:
    if ls in res:
        res[ls] += 1
    else:
        res[ls] = 1
result = [ls for ls in src if res[ls] == 1]
print(result)








# result = [23, 1, 3, 10, 4, 11]