'''
PythonChallenge5
Aria Outten 20180220
'''

import pickle

data = pickle.load(open('data/DataChallenge5.p', 'rb'))		# Open as binary
picture = ''		# Set blank variable

for line in data:		# Go through each [] set
	for word in line:		# Go through each () set
#		for each in range(word[1]):		# For each number add the symbol
#			picture = picture + word[0]
		picture = picture + word[0]*word[1]		# Alternative method used by Stephen
	picture = picture + '\n'		# Add a new line in the right place

print(picture)

