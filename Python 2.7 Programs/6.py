import random
def getAnswer(answerNumber):
	if answerNumber < 9 and answerNumber > 5:
		return 'Its is certain'
	elif answerNumber <= 5:
		return 'Fuck you'
		
r = random.randint(1,9)
print (r)
fortune =getAnswer(r)
print("r :" + str(r) + " " + fortune)