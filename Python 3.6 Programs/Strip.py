#This is regex version of Strip created in python to get hold of regex concepts

import re
def strip(str,chr=""):
	if(chr==""):
		finalStr=re.compile(r'\S+').match(str)
		return finalStr
	else:
		val=str.find(chr)
		lenChr=len(chr)
		finalStr=str[0:val]+str[val+lenChr:len(str)]
		return finalStr

print("Enter a String")
str=input()
print("Enter characters in string to be removed.Press Enter to remove extra whitespace")
chr=input()
print(strip(str,chr))


#Original Regex----(^\w+\s.*\w$)|(^\w+$)