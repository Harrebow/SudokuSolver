from ast import Try
import random
import copy

grid = []
sudokuSolved = False
solvedCount = 0
nishioFlag = False
imposibleFlag = False

class Square:
    def __init__(self, id):
        self.id = id
        self.value = 0
        self.row = 0
        self.column = 0
        self.box = 0
        self.locked = False
        self.posValues = [1,2,3,4,5,6,7,8,9]

# assign column.value to square objects
for i in range(1,82):
    grid.append(Square(i))
    if grid[i-1].id %9 != 0 or grid[i-1].id == 0:
        grid[i-1].column = grid[i-1].id %9
    else:
        grid[i-1].column = 9

# assign row.value to square objects
count = 1
count2 = 1
for i in grid:
    if count < 9:
        i.row = count2
        count +=1
    else:
        i.row = count2
        count = 1
        count2 +=1

# assign box.value to square objects
count = 0
count2 = 0
for i in grid:
    if (i.id-1) % 27 == 0 and (i.id-1) != 0:
        count2 += 3
        count = 0
    if (i.id-1) % 9 == 0 and (i.id-1) != 0:
        count=0
    if (i.id-1) % 3 > 0 and (i.id-1) != 0:
        i.box = count+count2
    else:
        count +=1
        i.box = count+count2

# print row, column and box values for testing
def rowColumnBox():
    print("Row")
    for i in grid:
        if int(i.id) %9 != 0 or i.id == 0:
            print(str(i.row)+", ",end="")
        else:
            print(i.row)
    print("Column")
    for i in grid:
        if int(i.id) %9 != 0 or i.id == 0:
            print(str(i.column)+", ",end="")
        else:
            print(i.column)
    print("Box")
    for i in grid:
        if int(i.id) %9 != 0 or i.id == 0:
            print(str(i.box)+", ",end="")
        else:
            print(i.box)
    print("Locked")
    for i in grid:
        if int(i.id) %9 != 0 or i.id == 0:
            print(str(i.locked)+", ",end="")
        else:
            print(i.locked)

def printSukdoku(grid):
    print("")
    for i in grid:
        if int(i.id) %9 != 0 or i.id == 0:
            print(str(i.value)+" ",end="")
        else:
            print(i.value)
    print("")

def createSudoku():
    global printCount
    printCount = 0
    num = 0
    for m in range(int(num)):
        if num != 81:
            x = random.randrange(len(grid))
        else:
            x = m
        values = []
        for i in grid:
            if i.row == grid[x].row or i.column == grid[x].column or i.box == grid[x].box:
                if i.value not in values:
                    values.append(i.value)
        
        count = 9
        for i in range(1,10):
            if i in values:
                count -=1
        
        if count>=1:
            y = random.randrange(1, 10)
            while y in values:
                y = random.randrange(1, 10)
            grid[x].value = y
            grid[x].locked = True
        else:
            print("No free numbers in line row or box.",grid[x].id)

# Test grid 1:

    grid[0].value = 3
    grid[6].value = 1
    grid[10].value = 2
    grid[11].value = 6
    grid[12].value = 5
    grid[21].value = 2
    grid[22].value = 8
    grid[29].value = 2
    grid[33].value = 7
    grid[34].value = 1
    grid[37].value = 7
    grid[39].value = 9
    grid[41].value = 4
    grid[52].value = 9
    grid[55].value = 5
    grid[56].value = 1
    grid[58].value = 9
    grid[60].value = 8
    grid[63].value = 4
    grid[68].value = 5
    grid[75].value = 7
    grid[76].value = 3
    grid[78].value = 9
    grid[0].locked = True
    grid[6].locked = True
    grid[10].locked = True
    grid[11].locked = True
    grid[12].locked = True
    grid[21].locked = True
    grid[22].locked = True
    grid[29].locked = True
    grid[33].locked = True
    grid[34].locked = True
    grid[37].locked = True
    grid[39].locked = True
    grid[41].locked = True
    grid[52].locked = True
    grid[55].locked = True
    grid[56].locked = True
    grid[58].locked = True
    grid[60].locked = True
    grid[63].locked = True
    grid[68].locked = True
    grid[75].locked = True
    grid[76].locked = True
    grid[78].locked = True

# expected results:

    # 3 0 0 0 0 0 1 0 0
    # 0 2 6 5 0 0 0 0 0
    # 0 0 0 2 8 0 0 0 0
    # 0 0 2 0 0 0 7 1 0
    # 0 7 0 9 0 4 0 0 0
    # 0 0 0 0 0 0 0 9 0
    # 0 5 1 0 9 0 8 0 0
    # 4 0 0 0 0 5 0 0 0
    # 0 0 0 7 3 0 9 0 0

    # Sudoku checked and solved!

    # 3 8 7 6 4 9 1 5 2
    # 9 2 6 5 1 3 4 8 7
    # 5 1 4 2 8 7 3 6 9
    # 6 9 2 3 5 8 7 1 4
    # 1 7 5 9 6 4 2 3 8
    # 8 4 3 1 7 2 5 9 6
    # 7 5 1 4 9 6 8 2 3
    # 4 3 9 8 2 5 6 7 1
    # 2 6 8 7 3 1 9 4 5

# Test grid 2:

    # grid[0].value = 2
    # grid[7].value = 4
    # grid[11].value = 8
    # grid[12].value = 3
    # grid[15].value = 2
    # grid[18].value = 9
    # grid[23].value = 1
    # grid[26].value = 7
    # grid[27].value = 4
    # grid[28].value = 6
    # grid[30].value = 9
    # grid[34].value = 1
    # grid[42].value = 7
    # grid[43].value = 9
    # grid[49].value = 8
    # grid[56].value = 3
    # grid[64].value = 5
    # grid[65].value = 2
    # grid[67].value = 3
    # grid[69].value = 9
    # grid[75].value = 8
    # grid[76].value = 6
    # grid[80].value = 4
    # grid[0].locked = True
    # grid[7].locked = True
    # grid[11].locked = True
    # grid[12].locked = True
    # grid[15].locked = True
    # grid[18].locked = True
    # grid[23].locked = True
    # grid[26].locked = True
    # grid[27].locked = True
    # grid[28].locked = True
    # grid[30].locked = True
    # grid[34].locked = True
    # grid[42].locked = True
    # grid[43].locked = True
    # grid[49].locked = True
    # grid[56].locked = True
    # grid[64].locked = True
    # grid[65].locked = True
    # grid[67].locked = True
    # grid[69].locked = True
    # grid[75].locked = True
    # grid[76].locked = True
    # grid[80].locked = True

# expected results:

    # 9 0 0 0 0 1 0 0 7
    # 4 6 0 9 0 0 0 1 0
    # 0 0 0 0 0 0 7 9 0
    # 0 0 0 0 8 0 0 0 0
    # 0 0 3 0 0 0 0 0 0
    # 0 5 2 0 3 0 9 0 0
    # 0 0 0 8 6 0 0 0 4

    # Sudoku checked and solved!

    # 2 7 6 5 9 8 1 4 3
    # 5 1 8 3 4 7 2 6 9
    # 9 3 4 6 2 1 5 8 7
    # 4 6 7 9 5 3 8 1 2
    # 3 8 5 4 1 2 7 9 6
    # 1 2 9 7 8 6 4 3 5
    # 8 4 3 2 7 9 6 5 1
    # 6 5 2 1 3 4 9 7 8
    # 7 9 1 8 6 5 3 2 4

# Test grid 3:

    # grid[14].value = 3
    # grid[16].value = 8
    # grid[17].value = 5
    # grid[20].value = 1
    # grid[22].value = 2
    # grid[30].value = 5
    # grid[32].value = 7
    # grid[38].value = 4
    # grid[42].value = 1
    # grid[46].value = 9
    # grid[54].value = 5
    # grid[61].value = 7
    # grid[62].value = 3
    # grid[65].value = 2
    # grid[67].value = 1
    # grid[76].value = 4
    # grid[80].value = 9
    # grid[14].locked = True
    # grid[16].locked = True
    # grid[17].locked = True
    # grid[20].locked = True
    # grid[22].locked = True
    # grid[30].locked = True
    # grid[32].locked = True
    # grid[38].locked = True
    # grid[42].locked = True
    # grid[46].locked = True
    # grid[54].locked = True
    # grid[61].locked = True
    # grid[62].locked = True
    # grid[65].locked = True
    # grid[67].locked = True
    # grid[76].locked = True
    # grid[80].locked = True

# expected results:

    # 0 0 1 0 2 0 0 0 0
    # 0 0 0 5 0 7 0 0 0
    # 0 0 4 0 0 0 1 0 0
    # 0 9 0 0 0 0 0 0 0
    # 5 0 0 0 0 0 0 7 3
    # 0 0 2 0 1 0 0 0 0
    # 0 0 0 0 4 0 0 0 9

    # Sudoku checked and solved!

    # 9 8 7 6 5 4 3 2 1
    # 2 4 6 1 7 3 9 8 5
    # 3 5 1 9 2 8 7 4 6
    # 1 2 8 5 3 7 6 9 4
    # 6 3 4 8 9 2 1 5 7
    # 7 9 5 4 6 1 8 3 2
    # 5 1 9 2 8 6 4 7 3
    # 4 7 2 3 1 9 5 6 8
    # 8 6 3 7 4 5 2 1 9

# Test grid 4: (Will fail!)

    # grid[0].value = 8
    # grid[11].value = 3
    # grid[12].value = 6
    # grid[19].value = 7
    # grid[22].value = 9
    # grid[24].value = 2
    # grid[28].value = 5
    # grid[32].value = 7
    # grid[40].value = 4
    # grid[41].value = 5
    # grid[42].value = 7
    # grid[48].value = 1
    # grid[52].value = 3
    # grid[56].value = 1
    # grid[61].value = 6
    # grid[62].value = 8
    # grid[65].value = 8
    # grid[66].value = 5
    # grid[70].value = 1
    # grid[73].value = 9
    # grid[78].value = 4
    # grid[0].locked = True
    # grid[11].locked = True
    # grid[12].locked = True
    # grid[19].locked = True
    # grid[22].locked = True
    # grid[24].locked = True
    # grid[28].locked = True
    # grid[32].locked = True
    # grid[40].locked = True
    # grid[41].locked = True
    # grid[42].locked = True
    # grid[48].locked = True
    # grid[52].locked = True
    # grid[56].locked = True
    # grid[61].locked = True
    # grid[62].locked = True
    # grid[65].locked = True
    # grid[66].locked = True
    # grid[70].locked = True
    # grid[73].locked = True
    # grid[78].locked = True

# expected results:

    # 8 0 0 0 0 0 0 0 0
    # 0 0 3 6 0 0 0 0 0
    # 0 7 0 0 9 0 2 0 0
    # 0 5 0 0 0 7 0 0 0
    # 0 0 0 0 4 5 7 0 0
    # 0 0 0 1 0 0 0 3 0
    # 0 0 1 0 0 0 0 6 8
    # 0 0 8 5 0 0 0 1 0
    # 0 9 0 0 0 0 4 0 0


    # 8 0 0 0 0 0 0 0 0
    # 0 0 3 6 0 0 0 0 0
    # 0 7 0 0 9 0 2 0 0
    # 0 5 0 0 0 7 0 0 0
    # 0 0 0 0 4 5 7 0 0
    # 0 0 0 1 0 0 0 3 0
    # 0 0 1 0 0 0 0 6 8
    # 0 0 8 5 0 0 0 1 0
    # 0 9 0 0 0 0 4 0 0

    # This sudoku is beyond the ability of this solver, requiring multiple nested guesses, or the sudoku is impossible to solve.
    

def calcNumbers():
    for i in grid:
        if i.locked == True:
            i.posValues = [0]
        else:
            for j in grid:
                if j.locked == True:
                    if j.row == i.row or j.column == i.column or j.box == i.box:
                        if j.value != 0:
                            if j.value in i.posValues:
                                i.posValues.remove(j.value)
                else:
                    if j.value != 0:
                        print("Error:",j.id,"id not locked and contains",j.value)
                        exit()

previousAttempts = []

def solveSudoku():
    global sudokuSolved, solvedCount, nishioFlag, grid, imposibleFlag, nishioGrid, nishioNum, backupGrid, previousAttempts

    def nishio(x):
        global nishioFlag, grid, nishioGrid, solvedCount, nishioNum, previousAttempts
        if x == False:
            for i in grid:
                if i.locked != True:
                    if i.id not in previousAttempts:
                        if len(i.posValues) == 2:
                            previousAttempts.append(i.id)
                            x=i
                            break
                    elif len(previousAttempts) >= 9:
                        exit()
            
            nishioNum = copy.deepcopy(x)
            grid[x.id-1].value = x.posValues[0]
            grid[x.id-1].locked = True
            calcNumbers()
            nishioFlag = True
        elif x == True:
            solvedCount -=1
            grid = copy.deepcopy(nishioGrid)
            grid[nishioNum.id-1].posValues = nishioNum.posValues
            grid[nishioNum.id-1].value = nishioNum.posValues[1]
            grid[nishioNum.id-1].locked = True
            calcNumbers()
            nishioFlag = "Nishio: Value option 2 Failed\n"
        else:
            exit()

    impossible = False
    count = len(grid)

    for i in grid:
        if i.locked != True:
            count -= 1

    if count < 81 and count != solvedCount:
        for i in grid:
            if i.locked != True:
                if len(i.posValues) < 1:
                    impossible = True
                    break
                elif len(i.posValues) == 1:
                    i.value = i.posValues[0]
                    i.locked = True
                    calcNumbers()
                else:
                        array1, array2, array3 = [],[],[]
                        array12, array22, array32 = [],[],[]
                        for j in grid:
                            if j.locked != True:
                                if j.row == i.row:
                                    for k in j.posValues:
                                        array1.append(k)
                                        array12.append(j.id)
                                if j.column == i.column:
                                    for k in j.posValues:
                                        array2.append(k)
                                        array22.append(j.id)
                                if j.box == i.box:
                                    for k in j.posValues:
                                        array3.append(k)
                                        array32.append(j.id)
        
                        list1 = [1,2,3,4,5,6,7,8,9]
                        for k in range(1,10):
                            if k not in array1:
                                list1.remove(k)
                        for k in list1:
                            if array1.count(k) == 1:
                                for n in grid:
                                    if n.id == array12[array1.index(k)]:
                                        n.value = k
                                        n.locked = True
                                        calcNumbers()

                        list1 = [1,2,3,4,5,6,7,8,9]
                        for k in range(1,10):
                            if k not in array2:
                                list1.remove(k)
                        for k in list1:
                            if array2.count(k) == 1:
                                for n in grid:
                                    if n.id == array22[array2.index(k)]:
                                        n.value = k
                                        n.locked = True
                                        calcNumbers()

                        list1 = [1,2,3,4,5,6,7,8,9]
                        for k in range(1,10):
                            if k not in array3:
                                list1.remove(k)
                        for k in list1:
                            if array3.count(k) == 1:
                                for n in grid:
                                    if n.id == array32[array3.index(k)]:
                                        n.value = k
                                        n.locked = True
                                        calcNumbers()
        if impossible != True:
            for j in grid:
                a = []
                for k in grid:
                    if k.box == j.box:
                        if j.locked != True and k.locked != True:
                            if len(k.posValues) == 2:
                                a.append(k)
                if len(a) == 2:
                    if a[0].column == a[1].column and a[0].posValues == a[1].posValues:
                        for k in grid:
                            if k.locked != True:
                                if k.column == a[0].column and k.box != a[0].box:
                                    for i in a[0].posValues:
                                        if i in k.posValues:
                                            if len(k.posValues) == 1:
                                                k.value = k.posValues[0]
                                                k.locked = True
                                                calcNumbers()
                                            else:
                                                k.posValues.remove(i)
                        a = []
                    elif a[0].row == a[1].row and a[0].posValues == a[1].posValues:
                        for k in grid:
                            if k.locked != True:
                                if k.row == a[0].row and k.box != a[0].box:
                                    for i in a[0].posValues:
                                        if i in k.posValues:
                                            if len(k.posValues) == 1:
                                                k.value = k.posValues[0]
                                                k.locked = True
                                                calcNumbers()
                                            else:
                                                k.posValues.remove(i)
                        a = []
                    calcNumbers()
        
        if impossible == True:
            if imposibleFlag != True:
                imposibleFlag = True
                nishio(True)
                calcNumbers()
                solveSudoku()
            else:
                nishioFlag = False
                impossible = False
                imposibleFlag = False
                grid = copy.deepcopy(backupGrid)
                nishioGrid = copy.deepcopy(grid)
                nishio(False)
                calcNumbers()
                solveSudoku()
        else:
            calcNumbers()
            solvedCount = count
            solveSudoku()

    else:
        if count != solvedCount:
            sudokuSolved = True
            if checkSolved():
                print("Sudoku checked and solved!")
                printSukdoku(grid)
            else:
                print(checkSolved(),"Try Again.")
                printSukdoku(grid)
        else:
            if nishioFlag == False:
                nishioGrid = copy.deepcopy(grid)
                backupGrid = copy.deepcopy(grid)
                nishio(False)
                calcNumbers()
                solveSudoku()
            elif nishioFlag == True:
                imposibleFlag = True
                nishio(True)
                calcNumbers()
                solveSudoku()
            else:
                nishioFlag = False
                impossible = False
                imposibleFlag = False
                grid = copy.deepcopy(backupGrid)
                nishioGrid = copy.deepcopy(grid)
                nishio(False)
                calcNumbers()
                solveSudoku()
                            
def checkSolved():
    flag = True
    if flag == True:
        for i in grid:
            for j in grid:
                if j.row == i.row or j.column == i.column or j.box == i.box:
                    if j.id != i.id and j.value == i.value:
                        flag = True
                    else:
                        flag = False
    if flag == True:
        return False
    else:
        return True

try:
    createSudoku()
    printSukdoku(grid)
    lkj = copy.deepcopy(grid)
    calcNumbers()
    solveSudoku()

except:
    printSukdoku(grid)
    print("This sudoku is beyond the ability of this solver, requiring multiple nested guesses, or the sudoku is impossible to solve.")

