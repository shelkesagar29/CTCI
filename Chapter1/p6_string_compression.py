import unittest

def solution1(string):
    """
    Time Complexity: O(N) where N is the length of the input string
    Space Complexity: O(1)
    """
    if not string:
        return ""
    last_char = string[0]
    last_count = 1
    r = ""
    # if all characters are different in given string i.e. count of each
    # character is one, string length does not change.
    # This varaible keeps track fo that on fly
    is_count_greater_than_one = False
    for i in range(1, len(string)):
        if last_char!=string[i]:
            r+=last_char
            r+=str(last_count)
            if last_count>1 and not is_count_greater_than_one:
                is_count_greater_than_one = True
            last_char = string[i]
            last_count = 1
        else:
            last_count+=1
    # add last left character to return string
    if last_count:
        r+=last_char
        r+=str(last_count)
        if last_count>1 and not is_count_greater_than_one:
            is_count_greater_than_one = True
    # if encoded and original string length is same, return original string
    if not is_count_greater_than_one or len(r)==len(string):
        return string
    else:
        return r

class TestClass(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()
