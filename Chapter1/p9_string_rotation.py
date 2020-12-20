import unittest

def is_substring_naive(main_string, sub_string):
    """
    e.g.
    main_string = abcbcglx   length = m
    sub_string = bcgl        length = n
    Time Complexity: O(m.n)
    Space Complexity: O(1)
    """
    c_i = 0
    while c_i < (len(main_string)-len(sub_string)):
        msri = c_i
        ssri = 0
        is_found = True
        while ssri < len(sub_string):
            if main_string[msri]==sub_string[ssri]:
                ssri+=1
                msri+=1
            else:
                is_found = False
                break
        if is_found:
            return True # start_index = c_i, end_index = msri-1
            break
        c_i+=1
    return False


def is_substring_kmp(main_string, sub_string):
    """
    e.g.
    main_string = abcbcglx   length = m
    sub_string = bcgl        length = n
    """
    pass

def solution1(string1, string2):
    """
    If original string is added with its own copy,
    rotated string will be part of it.
    """
    if len(string1)==len(string2):
        temp = 2*string1
        return is_substring_naive(temp, string2)
    return False

class TestClass(unittest.TestCase):
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]
    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for s1,s2, e_output in self.test_cases:
                self.assertEqual(test_function(s1, s2), e_output)

if __name__ == "__main__":
    unittest.main()
