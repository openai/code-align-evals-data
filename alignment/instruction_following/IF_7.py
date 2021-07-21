def my_func():
    def g(a, b):
        return a - b

    x = 1
    y = 2
    g(x, y)

    # Please call g again with the argument order reversed

    # END OF CONTEXT
    g(y, x)
    # END OF SOLUTION


def check(candidate):
    import inspect

    source = inspect.getsource(candidate)
    lines = source.strip().split("\n")


    # remove comments
    lines = [l for l in lines if l.strip() and l.strip()[0] != "#"]

    assert lines[-1].strip().replace(" ", "") == "g(y,x)"


if __name__ == "__main__":
    check(my_func)