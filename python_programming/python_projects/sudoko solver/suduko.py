import random
table =  [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
def valid(table,i,j,num):
    column =  [table[c][j] for c in range(len(table))]
    row = [table[i][c] for c in range(len(table))]
    if(num in column or num in row):
            return False
    box_row = (i//3)*3
    box_column = (j//3)*3
    for i in range(3):
        for j in range(3):
            if table[box_row+i][box_column +j] == num:
                return False
    return True



def solve(table):
    for i in range(len(table)):
        for j in range(len(table)):
            change = (table[i][j]==0)
            if(change):
                for num in range(1,len(table)+1):
                   if valid(table,i,j,num):
                    table[i][j] = num
                    if solve(table):
                        return True
                    table[i][j] = 0
                return False
    return True
                        
                    
if(solve(table)):        
    for rows in table:
        print(rows)
else:
    print("no solution")

