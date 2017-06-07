total =0
for num in range(101):
	total =total + num
print(total)

for i in range(12,16):
	print(i)
	
for i in range(0,10,2):
	print (i)
	
	
for i in range(5,-1,-1):
	print (i)
	
import random
for i in range(5):
	print(random.randint(1,10))
	
import sys
while True:
	print('Type exit to exit')
	response= raw_input()
	if response == 'exit':
		sys.exit()
	print('You typed' + response + ".")