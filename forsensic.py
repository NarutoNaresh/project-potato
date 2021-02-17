import os
mycwd=os.getcwd()
dircontents=os.listdir(mycwd)
for n in dircontents:
	print(n)
