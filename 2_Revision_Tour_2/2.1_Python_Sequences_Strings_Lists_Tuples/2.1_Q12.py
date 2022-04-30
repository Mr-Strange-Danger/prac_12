#User using Visual Studio Code
#User using Git feature from Visual Studio Code


a = [[1,2,3],
     [4,5,6],
     [7,8,9]]
row = len(a)
col = len(a[0])
n = row*col//2
count = 0
for r in range(row):
    for c in range(col):
        if count<=n:
            temp = a[r][c]
            a[r][c] = a[row-1-r][col-1-c]
            a[row-1-r][col-1-c] = temp
            count+=1 
for i in  range(row) :  
    for j in range(col) : 
        print(a[i][j],end= ' '); 
    print()
