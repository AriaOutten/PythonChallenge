'''
PythonChallenge7
Aria Outten 20180225
'''

from PIL import Image, ImageFilter

im = Image.open('data/oxygen.png')	# Open and load image
pix = im.load()

temp = ''		# Set empty variables
letters = []
answer = ''
dest = ''

for i in range(0,629,7):		# Go through the line
	if pix[i,45] == pix[i+1,45]:	# Stopping where the grey stops
		temp = pix[i,45]		# Take the number and add to the list
		letters.append(temp[0])

for i in letters:		# Convert the numbers to ascii
	answer += chr(i)

start = answer.find('[')		# Find the start of destination, remove the spaces then split at the ,
ans = answer[start+1:-1]
ans = ans.replace(' ','')
ans = ans.split(',')

for i in ans:		# Take each new no and convert to letters
	dest += chr(int(i))

print(answer)
print(dest)
