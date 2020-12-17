import unittest

def solution1():
    # Start first solution here
    pass

class TestClass(unittest.TestCase):
    test_cases = [

    ]

    test_functions = []

    def test_template(self):
        for test_function in self.test_functions:
            for t_input, e_output in self.test_cases:
                self.assertEqual(test_function(t_input), e_output)

if __name__ == "__main__":
    unittest.main()
