#!/usr/bin/python3
#Implementing Selection Sort in python
#Run Time Complexity:Best-O(n+k)
#Run Time Complexity:Average-O(n+k)
#Run Time Complexity:Worst-O(n+k)
#Space Complexity-O(n+k)
#Only apply for small integers when frequency of integers is more thatn integers

arr=[8,1,2,3,6,4,3,9]

def countingSort(arr):

	max1=max(arr)
	count = [0 for i in range(max1 + 1)]
	output = [0 for i in range(len(arr))]
	for i in arr:
		count[i]+=1

	for i in range(1,max1+1):
		count[i] += count[i-1]

	for i in range(len(arr)):
		output[count[arr[i]]-1]= arr[i]
		count[arr[i]]-=1
	
	return output	

print(countingSort(arr))






