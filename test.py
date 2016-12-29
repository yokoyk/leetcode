def removeDuplicates(lists):
    if len(list) == 0 || len(list) == 1:
        return len(list)
    count = 0
    for i in range(len(list) - 1) :
        if list[i] == list[i + 1]:
            continue
        else:
            count += 1
    return count
list = [1,2,3,1,2,4]
removeDuplicates(list)

















#































# https://leetcode.com/problems/count-and-say/
# def count_say(n):
# 	seq = ['1'];
# 	top = 1;
# 	while n - 1 > 0:
# 		n -= 1;
# 		index = 0;
# 		bak = []
# 		i = 0
# 		while i < top:
# 			num = 1
# 			while i + 1 < top and seq[i + 1] == seq[i]:
# 				i += 1;
# 				num += 1
# 			bak.append(chr(num + ord('0')) )
# 			print(bak)
# 			print("dddddddddd",ord('0'))
# 			bak.append(seq[i])
# 			i += 1
# 		seq = bak;
# 		top = len(bak)
# 	print(''.join(seq))
#
# count_say(5)










# def lengthOfLastWord( s):
# 	str = s.strip().split()
# 	return str[-1]




# def isPalindrome(s):
# 	if not s:
# 		return  True
# 	str = s.lower()
#
# 	begin = 0
# 	end =  len(str) - 1
# 	while begin < end:
# 		if not str[begin].isalnum():
# 			begin +=1
# 			continue
# 		if not str[end].isalnum():
# 			end -=1
# 			continue
# 		if str[begin] == str[end]:
# 			begin +=1
# 			end -=1
# 		else:
# 			return False
# 	return True




# def longestPalindrome(s):
# 	if not s:
# 		return ""
# 	result = ""
# 	pointer = 0
#
# 	while pointer <len(s)-1:
# 		begin, end = pointer - 1, pointer + 2
# 		while begin < 0 or end > len(s) - 1:
# 			tmp = s[begin,end]
# 			if isPalindrome(tmp) and len(tmp)>len(result):
# 				result = s[begin,end]
# 			begin -= 1
# 			end += 1
# 	pointer +=1
#
# 	return result
#
#
# def isPalindrome(s):
# 	if not s:
# 		return False
# 	return s == s[::-1]

