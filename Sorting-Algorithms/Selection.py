#Implementing Selection Sort in python
#Run Time Complexity:Best-(n*n)
#Run Time Complexity:Average-(n*n)
#Run Time Complexity:Worst-(n*n)
#Space Complexity-O(1)

arr=[9,6,4,8,7,5,1,2,3]
for i in range(len(arr)):
	for j in range(i+1,len(arr)):
		#Finds smallest element and brings it to the first position.
		#1 Less iteration after each consequetive loop
		if arr[j] < arr[i]: 
			arr[i],arr[j] = arr[j],arr[i]

print(arr)