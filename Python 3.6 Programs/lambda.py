#This is a demonstration of lambda function and how easy it is to use one.

def myFunc(list):
	prod_list = []
	for x in range(10):
		for y in range(5):
			product = x * y
			prod_list.append(product)
	return prod_list + list

print(myFunc([100,101,102]))

b=lambda list:[x*y for x in range(10) for y in range(5)]+ list

print(b([100,101,102]))
