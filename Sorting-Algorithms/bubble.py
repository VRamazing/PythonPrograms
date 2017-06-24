#Implementing Bubble Sort in python
#Run Time Complexity:Best-(n*n)
#Run Time Complexity:Average-(n*n)
#Run Time Complexity:Worst-(n*n)
#Space Complexity-O(1)

arr=[9,8,7,6,5,4,3,2,1]

def bubbleSort(arr):
	print("Original List : " + str(arr))
	for i in range(0,len(arr)):
		for j in range(0,len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]	
	print("Sorted List : " + str(arr))

bubbleSort(arr)
