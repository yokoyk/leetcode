def subarraysum(list):
	hash = {0 : -1}
	result = []
	sum  = 0
	for i in range(len(list)):
		sum += list[i]
		if sum == 0:
			result.append(0)
			result.append(i)
			print (result)
			return  result
		if sum in hash:
			print ([hash[sum]+1, i ])
			return [hash[sum]+1, i ]
		hash[sum] = i
list = [0,2,3,4,5,6,-7,-2,-2]
subarraysum(list)

