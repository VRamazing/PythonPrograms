#Implementing Selection Sort in python
#Run Time Complexity:Best-O(n)
#Run Time Complexity:Average-O(n*n)
#Run Time Complexity:Worst-O(n*n)
#Space Complexity-O(1)
#Only good for numbers upto 10000 and list almost sorted.


arr=[9,8,7,6,5,4,3,2,1]
arr2=arr.copy()
def insertionSort(arr):
	print("Original List : " + str(arr))
	for i in range(1,len(arr)):
		for j in range(i,0,-1):
			if arr[j] < arr[j-1]:
				arr[j],arr[j-1] = arr[j-1],arr[j]
			
	print("Sorted List : " + str(arr))

#Without Swapping.About 2x Faster than previous.This is shifting
def insertionSort2(arr):
	print("Original List : " + str(arr))
	for i in range(1,len(arr)):
		curr=arr[i]
		for j in range(i-1,0,-1):
			if curr < arr[j]:
				arr[j+1] = arr[j]
			arr[j]=curr
			
	print("Sorted List : " + str(arr))

insertionSort(arr)

insertionSort2(arr2)
