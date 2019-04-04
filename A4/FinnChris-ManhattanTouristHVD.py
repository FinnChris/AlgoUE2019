#/usr/bin/python3

import sys

#function to convert a nested list of strings to a nested list of floats
def nested_list_float(list):
    result = []
    for row in list:
        new_row = []
        for element in row:
            new_row.append(float(element))
        result.append(new_row)
    return result

#read input from stdin
input_list = sys.stdin.readlines()
#input_list = open("random_matrices/rmHV_10_21","r")

#read data into nested lists
in_down = False
in_right = False
in_diag = False
down = []
right = []
diag = []

for line in input_list:
    line.strip("\n")
    if "G_down" in line:
        in_down = True
        continue
    elif "G_right" in line:
        in_right = True
        continue
    elif "G_diag" in line:
        in_diag = True
        continue
    elif "---" in line:
        in_down = in_diag = in_right = False
        continue

    if in_down:
        down.append(line.split())
    elif in_right:
        right.append(line.split())
    elif in_diag:
        diag.append(line.split())

#convert nested list elements from string to float
down = nested_list_float(down)
right = nested_list_float(right)
diag = nested_list_float(diag)

#check for consistency
r = 0
grid_col = len(down[0])
grid_row = len(right)

for row in down:
    r += 1
    if len(row) != len(down[0]):
        sys.exit("Error: incorrect number of elements in row " + str(r) + " of g_down matrix. " + str(len(down[0])) + " elements expected.")

r = 0
for row in right:
    r += 1
    if len(row) != len(right[0]):
        sys.exit("Error: incorrect number of elements in row " + str(r) + " of g_right matrix. " + str(len(right[0])) + " elements expected.")

if (len(down) + 1) != len(right):
    sys.exit("Error: different number of rows according to g_down and g_right.")
if (len(down[0]) - 1) != len(right[0]):
    sys.exit("Error: different number of columns according to g_down and g_right.")
if (grid_col - 1 != len(diag[0]) or grid_row - 1 != len(diag)):
    sys.exit("Error: incorrect number of dimensions in matrix G_diag.")


#calculate number of columns and rows
ncol = len(down[1])
nrow = len(right)

#initialize scoring matrix
scoring_matrix = []

#fill first row
row_1 = [0]
for e in range(1,ncol,1):
    row_1.append(row_1[e - 1] + right[0][e - 1])
scoring_matrix.append(row_1)

#fill all other rows with larger value (horizontal vs vertical)
for row in range(1,nrow,1):
    scoring_matrix.append([scoring_matrix[row - 1][0] + down[row - 1][0]])
    for col in range(1,ncol,1):

        vertical = scoring_matrix[row - 1][col] + down[row - 1][col]
        horizontal = scoring_matrix[row][col - 1] + right[row][col - 1]
        diagonal = scoring_matrix[row - 1][col - 1] + diag[row - 1][col - 1]

        if horizontal >= vertical and horizontal >= diagonal:
            scoring_matrix[row].append(horizontal)
        elif vertical > horizontal and vertical >= diagonal:
            scoring_matrix[row].append(vertical)
        elif diagonal > horizontal and diagonal > vertical:
            scoring_matrix[row].append(diagonal)
        else:
            exit("Error: horizontal not larger smaller or equal to vertical!")
#return result to stdout
print(scoring_matrix[ncol - 1][nrow - 1])
