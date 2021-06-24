def my_func():
    # Please create 3 empty lists named a, b, and c.
    # END OF CONTEXT
    a = []
    b = []
    c = []
    # END OF SOLUTION


def check(candidate):
    import inspect

    source = inspect.getsource(candidate)
    lines = source.strip().split("\n")
    # remove comments
    lines = [l for l in lines if l.strip() and l.strip()[0] != "#"]
    assert lines[-3].strip().replace(" ", "") == "a=[]"
    assert lines[-2].strip().replace(" ", "") == "b=[]"
    assert lines[-1].strip().replace(" ", "") == "c=[]"


if __name__ == "__main__":
    check(my_func)