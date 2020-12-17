import unittest

def solution1(string):
    """
    Here we take advantage of the fact that,
    'Set' data stutcrure can hold only unique elemenets and look up time is O(1).
    Time Complexity: O(N)
    Space Complexity: O(N)
    Where N is length of the input string
    """
    if not string:
        return True
    temp_set = set()
    for c in string:
        if c in temp_set:
            return False
        else:
            temp_set.add(c)
    return True

def solution2(string):
    """
    This solution is again based on the concept of data structure 'Set'.
    Since 'Set' can hold only unique characters (in general objects), if we pass 
    a string with duplicate characters to 'Set', duplicates are removed.

    Thus string has all unique characters if number of elemnets in the set are exactly same
    as string length.

    Time Complexity: O(N)
    Space Complexity: O(N)
    where N is length of the input string.
    """
    return len(set(string))==len(string)


def solution3(string):
    """
    Here we consider string is made of ASCII characters and check whether characters 
    are repeated.

    NOTE* There are total 128 ASCII characters
    Time COmplexity: O(N)
    Space Complexity: O(1)
    where N is the length of the input string
    """
    if len(string)>128:
        return False
    
    char_list = [False]*128
    for c in string:
        if char_list[ord(c)]: # ord(c) gives ASCII value of the character.
            return False
        else:
            char_list[ord(c)]=True
    return True


class TestClass(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
    ]

    test_functions = [solution1, solution2, solution3]
    
    def test_is_unique(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()