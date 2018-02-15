'''
PythonChallenge2
Aria Outten 20180215
'''
import collections as c

data=open('data/DataChallenge2','r').read()  # Opens the file as the variable data

count=c.Counter(data)	# Lists all the characters and the number of their occurances

count=dict(count)   # Turns the variable into a dictionary type

answer = ''   # Sets a blank variable to be added to

for i in count:   # Checks for the characters which only occured once and adds it to the answer
	if (count[i]) == 1:
		answer += i

print (answer)
