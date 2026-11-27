input_str = input("nhập X,Y :")
dimention = [int(x) for x in input_str.split(',')]
rowNum = dimention[0]
colNum = dimention[1]

multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]=row*col

print(multilist)