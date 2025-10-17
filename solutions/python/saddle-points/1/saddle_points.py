def saddle_points(matrix):
    # Validar matriz
    if len(matrix) == 0:
        return []
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    num_row = len(matrix)
    num_col = len(matrix[0])

    cadidates = []

    for i in range(num_row):
        row = matrix[i]
        max_in_row = max(row)

        for j in range(num_col):
            if  row[j] == max_in_row:
                col = [matrix[k][j] for k in range(num_row)]
                min_in_col = min(col)
                if row[j] == min_in_col:
                    cadidates.append({"row":i+1, "column": j+1})
    return cadidates
