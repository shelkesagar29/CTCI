import unittest

def solution1(array):
    """
    Time Complexity: O(NxM) where NxM is array dimension
    Space Complexity: O(M+N) since we can in worst case save all row and column indices.
    """
    # Naive solution
    rows_with_zeros = set()
    cols_with_zeros = set()

    n_rows = len(array)
    n_cols = len(array[0])

    for r in range(n_rows):
        for c in range(n_cols):
            if not array[r][c]:
                if r not in rows_with_zeros:
                    rows_with_zeros.add(r)
                if c not in cols_with_zeros:
                    cols_with_zeros.add(c)
    
    # Now set row and cols to zero.
    for r in rows_with_zeros:
        for c in range(n_cols):
            array[r][c] = 0
    for c in cols_with_zeros:
        for r in range(n_rows):
            array[r][c]=0
    
    return array

def solution2(array):
    """
    In first approach we used two sets to save rows and columns to be nullified.
    To use constant space, we use first row and first column instead to mark zero row
    or column position.
    Time Complexity: O(NxM)
    Space Complexity: O(1)
    """
    if not array:
        return

    n_rows = len(array)
    n_cols = len(array[0])

    # Since we are using first row and column as space to mark rows and columns to be zeroed,
    # first check whether they have any zeros or not
    first_row_zero = False
    first_column_zero = False
    
    for c in range(n_cols):
        if not array[0][c]:
            first_row_zero=True
    
    for r in range(n_rows):
        if not array[r][0]:
            first_column_zero = True

    # Now start from 1,1 and check for 0. If 0 is found in certain row and column, mark first row
    # and column
    for r in range(1, n_rows):
        for c in range(1, n_cols):
            if not array[r][c]:
                array[0][c] = 0
                array[r][0] = 0

    # Now iterate through entire matrix again starting from 1,1 and set element to zero if 
    # first row or column for that element is zero
    for r in range(1, n_rows):
        for c in range(1, n_cols):
            if array[0][c]==0 or array[r][0]==0:
                array[r][c] = 0

    # Go back to the first row and column.
    if first_row_zero:
        for c in range(n_cols):
            array[0][c] = 0
    if first_column_zero:
        for r in range(n_rows):
            array[r][0] = 0

    return array
    
class TestClass(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    test_functions = [solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()
