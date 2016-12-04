#! python3
# prints tables right justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

col = [0] * len(tableData)
for i in range(len(tableData)):
	for j in range(len(tableData[i])):
		if len(tableData[i][j]) > col[i]:
			col[i] = len(tableData[i][j])

for j in range(len(tableData[i])):
	i = 0
	while i < len(tableData):
		print(tableData[i][j].rjust(col[i]), end=' ')
		i += 1
	print()

