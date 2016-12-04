def commaSpace(inList):
	for i in range(len(inList)):
		if i == (len(inList) - 1):
			print('and ' + str(inList[i]))
		else:
			print(str(inList[i]) + ', ' , end='')
			
spam = ['apples', 'bananas', 'tofu', 'cats', 42, 37, '/n']

commaSpace(spam)
