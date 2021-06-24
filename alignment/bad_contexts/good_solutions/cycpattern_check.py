def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

    l = len(b)
    pat = b + b
    for i in range(len(a) - l + 1):
        for j in range(l + 1):
            if a[i:i+l] == pat[j:j+l]:
                return True
    return False

def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("abcd","abd") == False , "test #0"
    assert  candidate("hello","ell") == True , "test #1"
    assert  candidate("whassup","psus") == False , "test #2"
    assert  candidate("abab","baa") == True , "test #3"
    assert  candidate("efef","eeff") == False , "test #4"
    assert  candidate("himenss","simen") == True , "test #5"

if __name__ == '__main__':
    check(cycpattern_check)
