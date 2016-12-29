def foursum(list, target):
    list.sort()
    results = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            k = j + 1
            z = len(list) - 1
            while k < z:
                sum = list[i] + list[j] + list[k] + list[z]
                if sum < target:
                    k += 1
                elif sum > target:
                    z -= 1
                else:
                    result = [list[i], list[j], list[k], list[z]]
                    z -= 1
                    k += 1
                    print(result)
                    if result not in results:
                        results.append(result)
            j += 1
        i += 1
    print(results)
    return  results

list = [1,2,3,4,6,-1,-2,5,8]
target = 10
foursum(list, target)
