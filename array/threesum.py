def threeSum(list, target):
	if len(list) <3 :
		return false
	results = []
  list.sort()
	for i in range(0,len(list) - 3):
		targets = target - list[i]
		hash = {}
		for j  in range(i + 1 ,len(list)):
			item = list[j]
			if  targets - item in hash:
				result = [list[i], list[j], targets - item ]
				if result not in results:
					results.append(result)
			else:
				hash[item] = j

	print (results)
	return  results

list = [1,2,3,7,4,5,6]
target = 10
threeSum(list , target)
