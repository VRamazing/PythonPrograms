supplies=['pen','staplers','flame-throwers','binders']
for i in range(len(supplies)):
	print('Index' + str(i) + 'in supplies is: ' + supplies[i])
	
print('pen' in supplies)
print('staplers' in supplies)
print('babba' in supplies)
print(supplies.index('binders'))
supplies.append('eraser')
print(supplies)
supplies.insert(2,'sharpner')
print(supplies)
supplies.remove('sharpner')
print(supplies)
supplies.sort()
print(supplies)
supplies.sort(reverse=True)
print(supplies)