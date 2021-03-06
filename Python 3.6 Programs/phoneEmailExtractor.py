#Phone Number and Email Address Extractor
import pyperclip,re

# Regex For Mobile Numbers
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				#areacode
	(\s|-|\.)?						#seperator
	(\d{3})							#first 3 digits
	(\d{4})							#last 4 digits 
	(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension  
	)''',re.VERBOSE)
	
# Regex For Email Address
emailRegex= re.compile(r'''(
	[a-zA-Z0-9._%+-]+				#username
	@								# @ symbol
	[a-zA-Z0-9.-]+					# domain name
	(\.[a-zA-Z]{2,4})               # dot-smething
	)''',re.VERBOSE)

	
#Find All Matches in Clipboard Text

text = str(pyperclip.paste())
matches=[]
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum + = ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])
	
#Copy Results to Clipboard

if len(matches) > 0
	pyperclip.copy('\n'.join(matches))
	print('Copies to clipboard:')
	print('\n'.join(matches))
ellse:
	print('No phone Number or email address found.')
