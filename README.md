# My Matrix

## Nicholas Norman, August 2024

As of August 2024, I am currently enrolled in a linear algebra course. We are practicing with augmented matrices and putting them in row reduced echelon form. So, as practice into the purview of linear algebra and computer science, I have tasked myself with doing my best to write a program that takes a matrix and row reduces it.

### Goal

The goal is to row reduce a matrix

### Input

The input is given by the user (or potentially a file). It will be an augmented matrix, representing a set of linear equations.

### Output

The output is the matrix in row reduced echelon form, defined by the folowing criteria:

* (a) Every pivot point must be a 1
* (b) All pivot points must descend
* (c) Every number above and below a pivot point must be a 0

### Steps

Here is an example augmented matrix, defined as 3 x 4, 3 variables and 3 equations

3x<sub>1</sub> + 5x<sub>2</sub> + 1x<sub>3</sub> = 4<br>
0x<sub>1</sub> + 2x<sub>2</sub> + 4x<sub>3</sub> = 5<br>
0x<sub>1</sub> + 0x<sub>2</sub> + 7x<sub>3</sub> = 2
```
[3 5 1 | 4]
[0 2 4 | 5]
[0 0 7 | 2]
```

#### Functions:

* Define elementary row operations:
    * Scale: multiply a row by a scalar value
    * Interchange: swap two rows
    * Add: Add a multiple of a row to another row
* isConsistent, checks if the system is consistent by looking for inconsistent rows ex. `[0 0 0 | 1]` 0x<sub>1</sub> + 0x<sub>2</sub> + 0x<sub>3</sub> = 1, (0 != 1)
* RowReduce, using the elementary operations, checks for consistency and reduced the matrix
* findPivot: finds the index of the pivot point of a row
* sort: sorts by depth of pivot point and row index
* descend: sort rows using interchange in descending order
* getLog: returns the log of operations
* clearLog: clears the log of opeartions

#### Examples

Scale ex.

2R<sub>2</sub> => R<sub>2</sub>
```
[3 5 1 | 4 ]
[0 4 8 | 10]
[0 0 7 | 2 ]
```
Interchange ex.

R<sub>1</sub> <=> R<sub>3</sub>
```
[0 0 7 | 2]
[0 2 4 | 5]
[3 5 1 | 4]
```
Add ex.

-2R<sub>1</sub> + R<sub>2</sub> => R<sub>2</sub>
```
[3  5  1 |  4]
[0 -8 -2 | -3]
[0  0  7 |  2]
```

### Using the Matrix Object

Constructor: `myMatrix = Matrix(matrix)`<br>
Null Constructor also works.

The Matrix object has a constructor that takes 1 parameter, the matrix that the user wants to represent. It must be a 2-dimensional list. An example is as such: `matrix = [[0,1,2,3],[4,5,6,7],[8,9,1,2]]`

`load()`: To change the matrix or load after constructing use `myMatrix.load(matrix)`

`display(decimal)`: This displays the matrix in a readable format. `decimal` respresents the amount of digits to round to in python's `round()` function.

`isConsistent()`: Returns `True` if a consistent matrix, definined as having at least one solution.

`rowReduce()`: Reduces the matrix to row reduced echelon form as defined by:

* (a) Every pivot point must be a 1
* (b) All pivot points must descend
* (c) Every number above and below a pivot point must be a 0

When performing a row reduction, the operations performed can be given as a list to the user.

`getLog()`: Returns a list of each operation (in human reable/math format).

`clearLog()`: clears the log. Note: the log never clears automatically.

### Example of use

```py
#define a set of linear equations
#x1 = 2
#x2 = 5
#x3 = 7

#2x1 + 3x2 + x3 = 26
#      x2 + x3 = 12
#      4x2 + 2x3 = 34

matrix = [
    [2,3,1,26],
    [0,1,1,12],
    [0,4,2,34]]

myMatrix = Matrix(matrix)
#myMatrix.load(matrix) #another way to load a matrix

myMatrix.display(3) #display to 3 digits

myMatrix.rowReduce() #row reduce

print("reducing:\n\noperations:") #prints operations from the log

log = myMatrix.getLog()
for i in log:
    print(i)

print("")

myMatrix.display(3)

myMatrix.clearLog() #clear the log after one use
```

This outputs as such:

```
| 2 3 1 26 |
| 0 1 1 12 |
| 0 4 2 34 |
reducing:

operations:
0.5R1 => R1
1.0R2 => R2
-1.5R2 + R1 => R1
-4R2 + R3 => R3
-0.5R3 => R3
1.0R3 + R1 => R1
-1.0R3 + R2 => R2

| 1.0 0.0 0.0 2.0 |
| 0.0 1.0 0.0 5.0 |
| 0.0 0.0 1.0 7.0 |
```
