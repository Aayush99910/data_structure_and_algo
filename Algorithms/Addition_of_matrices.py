# Addition of matrices 
# adding two matrices that are same size 
# improvement make the matrixc automatically 

def make_array(matrix: list) -> list:
  matrixDimension = []
  for i in range(len(matrix)): 
    array = []
    for j in range(len(matrix[i])):
      array.append(0)
    matrixDimension.append(array)
  return matrixDimension

def addition(matrixA: list, matrixB: list) -> list:
  matrixC = make_array(matrix=matrixA)
  for i in range(len(matrixA)): 
    for j in range(len(matrixA[i])):
      matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
  return matrixC

print(addition([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]))