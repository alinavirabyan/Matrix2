def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    
    return result

def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    result = []
    
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    
    return result

def strassen_matrix_mult(A, B):
    n = len(A)
    
    if n == 1:  
        return [[A[0][0] * B[0][0]]]
    
    mid = n // 2  
    A11 = []
    A12 = []
    A21 = []
    A22 = []
    B11 = []
    B12 = []
    B21 = []
    B22 = []

    for i in range(mid):
        A11.append(A[i][:mid])
        A12.append(A[i][mid:])
        B11.append(B[i][:mid])
        B12.append(B[i][mid:])
    
    for i in range(mid, n):
        A21.append(A[i][:mid])
        A22.append(A[i][mid:])
        B21.append(B[i][:mid])
        B22.append(B[i][mid:])

    M1 = strassen_matrix_mult(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_mult(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_mult(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_mult(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_mult(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_mult(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_mult(subtract_matrices(A12, A22), add_matrices(B21, B22))

    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])
    
    return C


A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

B = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]


result = strassen_matrix_mult(A, B)
print("Matrix result ")
for row in result:
    print(row)
