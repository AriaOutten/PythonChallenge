'''
PythonChallenge6
Aria Outten 20180221
'''
import zipfile
from re import search

data = zipfile.ZipFile('data/channel.zip', 'r')
nothing = '90052'  # Starting nothing
a = ''  # Set empty variable
answer = ''

while True:
	name = nothing + '.txt'
	comment = str(data.getinfo(name).comment)		# Gets the comment
	answer += comment[-2]
	text = str(data.read(name))		#	Opens file as string
	a = search('ext nothing is ', text)    # Find where the nothing starts
	if a is None:   # No nothings means a change or the end
		answer = answer.replace('n', '\n')
		print(answer)
		break
	nothing = text[a.end():-1]   # Takes whole nothing from page

