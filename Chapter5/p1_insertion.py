import unittest

def solution1(n, m, i, j):
    """
    Convert intergers to binary strings and operate in strings.
    """
    n_bins = list(bin(n)[2:])
    m_bins = list(bin(m)[2:])
    assert (j-i+1)==len(m_bins)
    # Note, i and j are numbered with LSB on right most side. Array indexing happens in opposite direction
    n_start_index = len(n_bins)-j - 1
    n_end_index = len(n_bins)-i - 1
    n_i = n_start_index
    m_i = 0
    while n_i <= n_end_index:
        n_bins[n_i] = m_bins[m_i]
        n_i+=1
        m_i+=1
    return int(''.join(n_bins), 2)

def solution2(n, m, i, j):
    """
    Bit manupulation
    """
    # Create a mask to clear the bits between j and i (both inclusive) in number n
    n_bits = len(bin(n)[2:])
    m_bits = len(bin(m)[2:])
    ones = sum(2**i for i in range(m_bits))
    mask_left = ones << (j+1)
    mask_right = (1<<i)-1
    mask = mask_left | mask_right
    n_cleared = n & mask
    m = m<<i
    return n_cleared | m

class TestCases(unittest.TestCase):
    test_inputs = [
        (1024, 19, 2, 6, 1100)
    ]

    test_functions = [solution1, solution2]

    def test_solutions(self):
        for f in self.test_functions:
            for n, m, i, j, e in self.test_inputs:
                self.assertEqual(f(n, m, i, j), e)


if __name__ == "__main__":
    unittest.main()