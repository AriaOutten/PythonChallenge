'''
PythonChallenge4
Aria Outten 20180220
'''
import urllib.request as request
from re import search

baseurl='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

number = '12345'	# Starting nothing

a = ''	# Set empty variable

while True:		# Start loop
	link = request.urlopen(baseurl + number)	# Create full link
	page = str(link.read())		# Reads the link as a string
	a = search('next nothing is ', page)		# Find where the nothing starts
	if a is None:		# No nothings means a change or the end
		if search('Divide',page) is None:
			print(page)
			break
		number = str(int(number)//2)		# Divides by 2 as per message
		link = request.urlopen(baseurl + number)
		page = link.read()
		page = str(page)
		a = search('next nothing is ', page)
	start = a.end()		# Nothing starts at end of line
	number = page[start:-1]		# Takes whole nothing from page
