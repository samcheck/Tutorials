import random
def getAns(ansNum):
	if ansNum == 1:
		return 'It is certain'
	elif ansNum == 2:
		return 'It is decidedly so'
	elif ansNum == 3:
		return 'Yes'
	elif ansNum == 4:
		return 'No'
print(getAns(random.randint(1,4)))
