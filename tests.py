import unittest

from matrix import Matrix


class MatrixTest(unittest.TestCase):
    def test_matrix_add(self):
        a = Matrix(3, 3, 3 + 2j)
        b = Matrix(3, 3, 1 + 2j)
        c = a.add(b)
        self.assertEqual(c, Matrix(3, 3, 4 + 4j))

    def test_matrix_subtract(self):
        a = Matrix(3, 3, 3)
        b = Matrix(3, 3, 1)
        c = a.subtract(b)
        self.assertEqual(c, Matrix(3, 3, 2))

    def test_matrix_multiply(self):
        a = Matrix(2, 3, 2)
        b = Matrix(3, 4, 3)
        c = a.multiply(b)
        self.assertEqual(c, Matrix(2, 4, 18))
        d = c.multiply(2.0)
        self.assertEqual(d, Matrix(2, 4, 36.0))

    def test_matrix_equals(self):
        a = Matrix(3, 3, 1)
        b = Matrix(3, 3, 1.0 + 0j)
        c = Matrix(2, 3, 0)
        self.assertEqual(a.__eq__(b), True)
        self.assertEqual(b.__eq__(c), False)
        self.assertEqual(a.__eq__(4 + 9j), False)
