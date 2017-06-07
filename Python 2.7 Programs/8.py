
def collatz():
	if(number%2==0):
		print(str(number))
	else:
		print(str(3*number + 1))
		
while True:
	print('Type a number or \'exit\' for exiting')
	number = raw_input()
	if number== 'exit':
		break
	else:
		number=int(number)
	collatz()
	
	