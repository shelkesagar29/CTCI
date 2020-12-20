import unittest

def solution1(string):
    """
    This solution detects palindrome using counting
    rather than two pointer technique (Two pointer technique
    is important when order of characters in palindrome is preserved
    in test cases).
    1. Count occurance of each charater.
       Character occuring more than twice is rounded back
       i.e 3 ->1,  4->2, 5->1, 6->2 ...
    2. If string is palindrome, only one charater count should be 
    1. i.e. every other chracter should have its pair.
    """
    if not string:
        return True

    string = string.lower()
    # Palindrome based on count
    h_map = {}
    # get character count
    for c in string:
        if not c.isalnum():
            continue
        if c in h_map:
            h_map[c]+=1
            if h_map[c]>2:
                h_map[c]=1
        else:
            h_map[c]=1
    # check palindrome based on the count
    is_first = True
    for k in h_map.keys():
        if h_map[k]==1:
            if is_first:
                is_first=False
                continue
            else:
                return False
    return True

class TestClass(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]

    test_functions = [solution1]

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()
