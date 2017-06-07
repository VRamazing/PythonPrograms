spam = ['apples','bananas','tofu','cats','love']
final=spam[0]
for x in range(1,len(spam)-1):
	
	final = final +  ", "  + spam[x]
	if x==len(spam)-2:
		final = final + " and " + spam[len(spam)-1]

print final
	
