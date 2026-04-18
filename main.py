### This file represents the main file to be run.
### Nicholas Norman
### August 2024
### Guass-Elim

import copy

#goal: convert a matrix to row reduced echelon form
#input: augmented matrix given by the user
#output: the same matrix in row reduced echelon form

#define a matrix object to have functions inside

class Matrix:
    def __init__(self, matrix=None):
        self.height = 1
        self.width = 2
        self.data = []
        self.log = []

        if (matrix != None):
            self.load(matrix)

    def load(self, matrix):
        #goal: load a matrix into the system
        #input: a list representing a matrix
        #output: changes matrix object

        self.data = copy.deepcopy(matrix)

        self.height = len(matrix)
        self.width = len(matrix[0])
    
    def display(self, decimal):
        #goal is to print a matrix in a readable format
        #input: multidimensional array, integer
        #output: readable matrix

        for i in range(0, self.height):

            print("| ", end="")

            for j in range(0, self.width):
                print(round(self.data[i][j], decimal), end=" ")

            #line break
            print("|")

    def scale(self, row, scalar):
        #goal: multiply a row by a scalar value
        #input: matrix row that needs to be scaled
        #output: changed matrix

        for i in range(0, self.width):
            #multiply item by scalar value
            self.data[row][i] = self.data[row][i] * scalar

        self.log.append(f"{scalar}R{row+1} => R{row+1}")

    def interchange(self, row1, row2):
        #goal: interchange 2 rows
        #input: matrix and 2 rows
        #output: changed rows

        #basic swap function
        tmpRow = self.data[row2]
        self.data[row2] = self.data[row1]
        self.data[row1] = tmpRow

        self.log.append(f"R{row1+1} <=> R{row2+1}")

    def add(self, scalar, row1, row2):
        #goal add row 1 * scalar to row2 (scalar * row1) + row2 => row2
        #input: row1 to multiply by scalar and add to row2
        #output: new row2

        #for each column
        for i in range(0, self.width):
            self.data[row2][i] = (scalar * self.data[row1][i]) + self.data[row2][i]

        self.log.append(f"{scalar}R{row1+1} + R{row2+1} => R{row2+1}")

    def isConsistent(self):
        #goal: check if the matrix is consistent after a row reduction
        #input: matrix
        #output: true or false

        zeroCounter = 0

        #for each row
        for i in range(0, self.height):
            #if all coeff are 0 and constant = 0
            zeroCounter = 0

            for j in range(0, self.width - 1):
                if (self.data[i][j] == 0):
                    zeroCounter += 1
            
            #if # of zeros is the same as width, fail
            if (zeroCounter == self.width - 1 and self.data[i][-1] != 0):
                return False
            
            zeroCounter = 0

        return True
    
    def findPivot(self, row):
        #goal: get index of pivot point
        #input: matrix and row
        #output: index of pivot point

        #in row, go thru until a number is not a zero
        keepGoing = True
        index = 0
        while(keepGoing == True):

            if(self.data[row][index] != 0):
                keepGoing = False

            elif(index > self.width - 1):
            #if not a varibale, no pivot

                keepGoing = False
                index = -1

            else:
                index += 1
        
        return index
    
    def sort(self):
        #goal: sort rows by index in order of lest to most depth
        #input: matrix
        #output: a list of row indexes

        depth = []

        #for each row
        for j in range(0, self.height):
            #for each row, count zeros to pivot
            pivotIndex = self.findPivot(j)
            depth.append([pivotIndex, j]) #stores [depth, rowIndex]

        #sort by depth
        depth.sort()

        return depth
    
    def descend(self):
        #goal: sort in descending order
        #input: matrix
        #output: interchanged rows

        #for all rows
        for j in range(0, self.height):
            #sort
            depth = self.sort()
            #if sort-row index(1) == matrix-row index (j) #not already the same row
            if (depth[j][1] != j):
                #interchange sort[j][1] with matrix[j]
                self.interchange(depth[j][1], j)
    
    def rowReduce(self):
        #goal: row reduce the matrix into row reduced echelon form
        #input: matrix
        #output: matrix in RREF

        #interchange based on leading zeros
        self.descend()

        #for row in matrix
        for i in range(0, self.height):
            #find pivot point
            pivotIndex = self.findPivot(i)
            pivot = self.data[i][pivotIndex]

            #make sure there is a pivot!
            if (pivotIndex != -1):
                #scale pivot to 1
                self.scale(i, (1/pivot))

                #for every OTHER number above and below pivot
                for j in range(0,self.height):
                    #if not the current tab
                    if(j != i):
                        #if not a zero
                        if(self.data[j][pivotIndex] != 0):
                            #add operation to make 0
                            self.add(-1 * (self.data[j][pivotIndex]), i, j)

        
        #check consistency
        if(self.isConsistent() != True):
            #tell user that it is inconsistent
            print("This matrix is inconsistent")

    def getLog(self):
        #goal: return the log
        #input: nothing
        #output: log

        return self.log
    
    def clearLog(self):
        #goal: clear log
        #input: none
        #output: none

        self.log.clear()

if __name__ == "__main__":

    #input the matrix
    ##matrix = inputMatrix()

    #x1 = 2
    #x2 = 5
    #x3 = 7

    #2x1 + 3x2 + x3 = 26
    #      x2 + x3 = 12
    #      4x2 + 2x3 = 34

    matrix = [
        [1,-3,4,12],
        [1,-7,24,-76],
        [1,25,176,556]]

    myMatrix = Matrix(matrix)
    #myMatrix.load(matrix)
    
    myMatrix.display(3)

    myMatrix.rowReduce()

    print("reducing:\n\noperations:")

    log = myMatrix.getLog()
    for i in log:
        print(i)

    print("")

    myMatrix.display(3)

    myMatrix.clearLog()