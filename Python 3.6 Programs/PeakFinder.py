#PEAK FINDER
array1 = [1,2,3,4,5,6,7,8,9]
array2 = [9,8,7,6,5,4,3,2,1]
array3 = [1,2,3,4,5,4,3,2,1]
array4 = [9,8,7,6,5,6,7,8,9]
array5 = [1,2,2,4,4,4,4,4,4]

def peakfinder(arr):
	i=0
	peak=0
	while i < len(arr):
		if i==0:
			if arr[i]>arr[i+1]:
				peak=arr[i]
				break
			else:
				i=i+1
				continue
				
		elif i == len(arr)-1:
			if arr[i]>arr[i-1]:
				peak = arr[i]
				break
				
		if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
			peak = arr[i]
			break
		i=i+1

	if(peak==0):
		print("No Peak found")
	else:
		print("Peak is " + str(peak))
		
peakfinder(array1)
peakfinder(array2)
peakfinder(array3)
peakfinder(array4)
peakfinder(array5)
