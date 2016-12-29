def twoSum(list, target):
	hash = {}
	for i, item in enumerate(list):
		if target - item in hash:
			return (hash[target - item] , i)
		hash[item] = i
	return  (-1, -1)

list = [1,2,3,4,5,6,0,7,8,9]
target = 10
twoSum(list, target)
