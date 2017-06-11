import re
#Must be 8 characters long
#Have Both Upper case and Lower case alphabets and atleast 1 digit.


def checkStrongPass(pass1):
	passRegex=re.compile(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$')
	mo = passRegex.match(pass1)
	if mo==None:
		return "Password should be atleast 8 digit long containing atleast 1 capital letter and a digit.Alphabets and Special Characters are allowed."
	else:
		return "good  password"
		

print("Enter password")
pass1=input()
print(checkStrongPass(pass1))