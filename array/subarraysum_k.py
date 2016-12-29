def subarraysum(list , k):
	hash = {0 : -1}
	result = []
	sum  = k
	for i in range(len(list)):
		sum += list[i]
		if sum == k:
			result.append(0)
			result.append(i)
			print (result)
			return  result
		if sum-k in hash:
			print ([hash[sum-k]+1, i ])
			return [hash[sum-k]+1, i ]
		hash[sum] = i
list = [1,2,3,4,5,6,-7,-2,-2]
k = -5
subarraysum(list, k)
