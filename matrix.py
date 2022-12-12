class Matrix:
    def __init__(self, row_count, column_count, value):
        if column_count <= 0 or row_count <= 0:
            raise Exception(f"Matrix creation error! Unable to create a {row_count}x{column_count} matrix!")
        else:
            self.__rows = row_count
            self.__columns = column_count
            self.__matrix = [[value for _ in range(row_count)] for _ in range(column_count)]

    def get_column_count(self):
        return self.__columns

    def get_row_count(self):
        return self.__rows

    def get_element(self, row, column):
        if row > self.__rows or row < 0 or column < 0 or column > self.__columns:
            raise Exception("Index out of bounds!")
        else:
            return self.__matrix[row][column]

    def set_element(self, row, column, value):
        if row > self.__rows or row < 0 or column < 0 or column > self.__columns:
            raise Exception("index out of bounds!")
        else:
            self.__matrix[row][column] = value

    def add(self, matrix):
        if isinstance(matrix, Matrix):
            if self.__columns != matrix.__columns or self.__rows != matrix.__rows:
                raise Exception(
                    f"Can't add {self.__rows}x{self.__columns} matrix with"
                    f" {matrix.__rows}x{matrix.__columns} matrix")
            else:
                result_matrix = Matrix(self.__columns, self.__rows, 0)
                for i in range(result_matrix.__rows):
                    for j in range(result_matrix.__columns):
                        result_matrix.__matrix[i][j] = self.__matrix[i][j] + matrix.__matrix[i][j]

            return result_matrix
        else:
            raise Exception("Error! Argument is not a Matrix class")

    def subtract(self, matrix):
        if isinstance(matrix, Matrix):
            if self.__columns != matrix.__columns or self.__rows != matrix.__rows:
                raise Exception(
                    f"Can't subtract {self.__rows}x{self.__columns} matrix with"
                    f" {matrix.__rows}x{matrix.__columns} matrix")
            else:
                result_matrix = Matrix(self.__columns, self.__rows, 0)
                for i in range(result_matrix.__rows):
                    for j in range(result_matrix.__columns):
                        result_matrix.__matrix[i][j] = self.__matrix[i][j] - matrix.__matrix[i][j]

            return result_matrix
        else:
            raise Exception("Error! Argument is not a Matrix class")

    def __scalar_product(self, value):
        result_matrix = Matrix(self.__rows, self.__columns, 0)
        for i in range(result_matrix.__rows):
            for j in range(result_matrix.__columns):
                result_matrix.__matrix[i][j] = self.__matrix[i][j] * value

        return result_matrix

    def multiply(self, obj):
        if isinstance(obj, (int, float, complex)):
            return self.__scalar_product(obj)
        elif isinstance(obj, Matrix):
            if self.__columns == obj.__rows:
                result_matrix = Matrix(self.__rows, obj.__columns, 0)
                for i in range(result_matrix.__rows):
                    for j in range(result_matrix.__columns):
                        value = 0
                        for k in range(result_matrix.__rows):
                            value += self.__matrix[i][k] * obj.__matrix[k][j]
                        result_matrix.__matrix[i][j] = value
                return result_matrix
            else:
                raise Exception("The number of columns of the first matrix is not equal "
                                "to the number of rows of the second matrix!")

        else:
            raise Exception("Error! Argument must be of type int, float, complex, or Matrix")

    def transpose(self):
        result_matrix = Matrix(self.__rows, self.__columns, 0)
        for i in range(self.__rows):
            for j in range(self.__columns):
                result_matrix.__matrix[j][i] = self.__matrix[i][j]

        return result_matrix

    def __str__(self):
        return '\n'.join(' | '.join(map(str, row)) for row in self.__matrix)
