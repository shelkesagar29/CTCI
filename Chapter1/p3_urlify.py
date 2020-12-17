import unittest

def solution1(string, length):
    """
    Time Complexity: O(N) where N is length of the string
    """
    char_list = list(string)
    end_ptr = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # if character is space, add %20
            char_list[end_ptr-3:end_ptr] = "%20"
            end_ptr-=3
        else:
            # else character is not space, move character to the end
            char_list[end_ptr-1] = char_list[i]
            end_ptr-=1
    return "".join(char_list)
    

def solution2(string, length):
    """
    We use python string operations.
    """
    return string.rstrip().replace(" ", "%20")

class TestClass(unittest.TestCase):
    test_cases = [
        ("much ado about nothing      ", "much%20ado%20about%20nothing"),
        ("Mr John Smith    ", "Mr%20John%20Smith"),
    ]

    test_functions = [solution1, solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                actual_length = len(t_input.rstrip(" "))
                self.assertEqual(test_function(t_input, actual_length), e_output)

if __name__ == "__main__":
    unittest.main()
