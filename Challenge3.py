'''
PythonChallenge3
Aria Outten 20180215
'''
import re

data=open('data/DataChallenge3','r').read()  # Opens the file as the variable data

data = data.replace('\n','')		# Removes the newline characters that were inserted when it was read

answer = ''   # Sets a blank variable to be added to

for i in re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',data):   # Checks for the pattern and adds it to the answer
	a = i[4]
	answer += a

print (answer)
