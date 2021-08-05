#this code checks the md5 hash of a specific file. This is useful if
#you want to trigger an action based on a file change. 

import hashlib

#choose the var to use and which hash encoding you are going to use
hasher = hashlib.md5()

#open the file with read and binary "rb"
with open("userNames1.csv", "rb") as afile:

	#read the file
	buf = afile.read()

	#create hash of the file	
	hasher.update(buf)

#print the encoded has of the file specified above
print(hasher.hexdigest())