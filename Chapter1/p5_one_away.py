import unittest

def one_insert(string1, string2):
    # here string 2 is the smaller string
    s1 = 0
    s2 = 0
    inserted = False
    while s1<len(string1) and s2<len(string2):
        if string1[s1]!=string2[s2]:
            if inserted:
                return False
            inserted = True
            s1+=1
        else:
            s1+=1
            s2+=1
    return True

def one_replace(string1, string2):
    # If string length is not same, replace won't work!
    replaced = False
    s1 = 0
    s2 = 0
    while s1<len(string1):
        if string1[s1]!=string2[s2]:
            if replaced:
                return False
            replaced = True
        s1+=1
        s2+=1
    return True
                

def solution1(string1, string2):
    """
    We check for each condition separately.
    Args:
        string1: first input string
        string2: second input string
    Time Complexity: O(N) where N is the lngth of the longest of the two strings.
    Space COmpelxity: O(1) No extra space has been used
    """
    # Note all the operations are to be done on the second string
    # Here problem of removal is treated as insert into smaller string.
    ls1 = len(string1)
    ls2 = len(string2)
    if ls1==ls2:
        return one_replace(string1, string2)
    elif ls1 == ls2+1:
        # here string1 is bigger
        return one_insert(string1, string2)
    elif ls1 == ls2-1:
        # here string2 is bigger
        return one_insert(string2, string1)
    return False

def solution2(string1, string2):
    """
    This approach is based on the sets.
    e.g.
    x = {"a","b", "c"}
    y = {"c", "m", "a"}

    x&y (intersection of the two sets) gives us all the 
    common elements in the two sets. i.e. {"a","c"}
    """
    # Case for one replace
    if len(string1)==len(string2):
        if string1==string2:
            return True
        # if two strings have same length and they differ by only
        # one character, intersection of the sets of the two strings 
        # will have exactly one character less which compared to 
        # number of characters in both the strings.
        # e.g. x = "pale" -> set(x) = {'p', 'a', 'l', 'e'}
        #      y = "bale" -> set(y) = {'b', 'a', 'l', 'e'}
        # set(x)&set(y) = {'a', 'l', 'e'}
        if len(set(string1)&set(string2))==len(string1)-1:
            return True
    # case for insert or delete.
    # In this case, strings differe by exactly the length of one
    if abs(len(string1)-len(string2))==1:
        length_of_smaller_string = min(len(string1), len(string2))
        # Now intersection of the sets of two strings will be the length
        # of the size of the smaller string.
        # e.g.
        # x = "pale" -> set(x) = {'p', 'a', 'l', 'e'} 
        # y = "ple" -> set(y) = {'p', 'l', 'e'}
        # set(x)&set(y) = {'p', 'l', 'e'}
        if len(set(string1)&set(string2))==length_of_smaller_string:
            return True

    return False

class TestClass(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
    ]

    test_functions = [solution1, solution2]

    def test_template(self):
        for test_function in self.test_functions:
            for s1, s2, e_output in self.test_cases:
                self.assertEqual(test_function(s1, s2), e_output)

if __name__ == "__main__":
    unittest.main()
