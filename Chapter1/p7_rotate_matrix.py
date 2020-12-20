# Rotate matrix/image of size NxM clockwise by 90 degree.
import unittest

def solution1(array):
    """
    Time Complexity: O(NxM) where array is NxM dims
    Space Complexity: O(NxM) 
    """
    num_r_rows = len(array)
    num_r_cols = len(array[0])
    w = [[0 for _ in range(num_r_cols)] for _ in range(num_r_rows)]

    for r in range(num_r_rows):
        target_col = num_r_rows-r-1
        for c in range(num_r_cols):
            target_row = c
            w[target_row][target_col] = array[r][c]

    return w 

def solution2(array):
    """
    This approach rotates array in place.
    Time Complexity: O(NxM) where array is NxM dims
    Space Complexity: O(1)
    
    e.g.
    [[1,2,3],
     [4,5,6],
     [7,8,9]]

     First step is to transpose the matrix in place
    
    [[1,4,7],
     [2,5,8],
     [3,6,9]]

     Then use two point approach to swap elements row by row. (Treat each
     row as array reversal problem)
    
    [[7,4,1],
     [8,5,2],
     [9,6,3]]
    """
    n_rows = len(array)
    n_cols = len(array[0])

    # step 1. In place matrix transpose
    # We travel along the diagonal.
    r = 0
    c = 0
    while r<n_rows and c<n_cols:
        sr = r+1 # swap row start
        sc = c+1 # swap column start

        while sr<n_rows and sc < n_cols:
            temp = array[r][sc]
            array[r][sc] = array[sr][c]
            array[sr][c] = temp
            sr+=1
            sc+=1
        r+=1
        c+=1
    
    # step 2. Treat each rows as array reversal problem
    # and reverse rows
    for r in range(n_rows):
        si = 0
        ei = n_cols-1
        while si<ei:
            temp = array[r][ei]
            array[r][ei] = array[r][si]
            array[r][si] = temp
            si+=1
            ei-=1
    
    return array

class TestClass(unittest.TestCase):
    test_cases = [
        ([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
        ([[1,2],[3,4]],[[3,1],[4,2]]),
        ([[1]],[[1]])
    ]

    test_functions = [solution1, solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()
