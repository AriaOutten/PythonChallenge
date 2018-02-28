'''
PythonChallenge1
Aria Outten 20180214
'''

original = 'abcdefghijklmnopqrstuvwxyz. '
translate = 'cdefghijklmnopqrstuvwxyzab. '

message = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

answer = ''

#answer = message.translate(message.maketrans(original, translate)) # Based on answer's hint

for i in message:
	answer += translate[original.find(i)]

print (answer)
