def my_func():
    a = []
    # append(a, 1)
    # print(a)
    # b=a
    # Please write a corrected version of the commented line that has a syntax error
    # END OF CONTEXT
    print(a.append(1))
    # END OF SOLUTION


def check(candidate):
    import inspect

    source = inspect.getsource(candidate)
    lines = source.strip().split("\n")
    # remove comments
    lines = [l for l in lines if l.strip()[0] != "#"]
    assert lines[-1].strip().replace(" ", "") == "a.append(1)"


if __name__ == "__main__":
    check(my_func)