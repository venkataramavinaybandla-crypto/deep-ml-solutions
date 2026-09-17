def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # b = []
    # for i in range(len(a[0])):
    #     for j in range(len(a)):
    #         T = np.empty((j, i))
    #         a[i][j] = T[j][i]
    #         b = T
    
    # Print(b)
    T = []
    for i in range(len(a[0])):
        b = []
        for j in range(len(a)):
          b.append(a[j][i])
        T.append(b) 
    return T