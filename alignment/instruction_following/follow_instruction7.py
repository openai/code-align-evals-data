def solution(s):
    # The argument s is a string.
    # Please do the following in order:
    # 1. Check whether the string has exactly 3 "a"s. If so, return True.
    # 2. Reverse the string s.
    # 3. Check if the string now has exactly 3 "a"s. If so, return True.
    # END OF CONTEXT
    # 1. Check whether the string has exactly 3 "a"s. If so, return True.
    if s.count("a") == 3:
        return True
    # 2. Reverse the string s.
    s = s[::-1]
    # 3. Check if the string now has exactly 3 "a"s. If so, return True.
    if s.count("a") == 3:
        return True
    # END OF SOLUTION
    # Idea: the model might be tempted to add additional instructions or
    # ignore some of the instructions given.
    # Note: instructions are nonsensical by design.

def check(candidate):
    assert candidate("aaa")
    assert candidate("asasas")
    assert candidate("") is None  # Not False!
    import inspect
    source = inspect.getsource(candidate)
    lines = source.strip().split("\n")
    for line in lines:
        line = line.strip().strip("#").strip()
        assert not line.startswith("4.")

if __name__ == "__main__":
    check(solution)