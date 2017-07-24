
quotes = open('Quotes','r')
final = open('final','w')
quote = []
q = quotes.readlines()

while '\n' in q:
	q.remove('\n')

for i in q:
	main = i.split('.')
	text = main[1].strip()
	
	if len(main)==2:
		name = text.split('-')[1].strip()
	else:
		name = main[2].strip()
		name = name.split('-')[1]
	
	quote.append({'name':name,'text':text})


final.write(str(quote))
final.close()
quotes.close()
	


		
	

