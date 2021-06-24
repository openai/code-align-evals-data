def my_func():
    a = [1, 2, 3]
    # Please copy the line above, but with the variable name 'b' instead of 'a'.
    # END OF CONTEXT
    b = [1, 2, 3]
    # END OF SOLUTION


def check(candidate):
    import inspect

    source = inspect.getsource(candidate)
    lines = source.strip().split("\n")
    # remove comments
    lines = [l for l in lines if l.strip() and l.strip()[0] != "#"]
    assert lines[-1].strip().replace(" ", "") == "b=[1,2,3]"


if __name__ == "__main__":
    check(my_func)