"""
Permutation is just different arrangement of the string.
"""
import unittest

def solution1(string1, string2):
    """
    Since its just different arrangement of characters, sorted string should match.
    Sorting algorithm time complexity is O(NlogN) where N is length of sequence.

    Time Complexity: 
    We first sort both the arrays where time complexityof each sort is O(NlogN)
    O(NlogN)+O(MlogM) where N and M are the lengths of the strings
    Then we compare two arrays
    O(N)

    Final time complexity: O(NlogN)
    Space Complexity: O(1)    
    """
    if len(string1)!=len(string2):
        return False
    return sorted(string1)==sorted(string2)

def solution2(string1, string2):
    """
    We use hash table to compare whether exact number of characters are present in
    both the strings.
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    if len(string1)!=len(string2):
        return False
    # Add all characters from string one to 
    string1_chars = {}
    for c in string1:
        if c in string1_chars:
            string1_chars[c]+=1
        else:
            string1_chars[c]=1
    # check whether exact characetrs appear for exact number of times
    for c in string2:
        if c not in string1_chars:
            return False
        else:
            string1_chars[c]-=1
            if string1_chars[c]<0:
                # If count goes below zero, c is appearing in string2 more times.
                return False
    return True
    


class TestClass(unittest.TestCase):
    test_cases = [
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    ]

    test_functions = [solution1, solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input1, t_input2, e_output in self.test_cases:
                self.assertEqual(test_function(t_input1, t_input2), e_output)

if __name__ == "__main__":
    unittest.main()
