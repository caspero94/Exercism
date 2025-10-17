class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for fila in matrix_string.split("\n"):
            fila_temp = []
            for columna in fila.split():
                fila_temp.append(int(columna))
            self.matrix.append(fila_temp)
        print(self.matrix)
        
    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        colum_temp = []
        for x in self.matrix:
            colum_temp.append(x[index-1])
        return colum_temp