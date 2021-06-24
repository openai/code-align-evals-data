def my_func():
    a = 0
    # Please print the name of this function
    # END OF CONTEXT
    print("my_func")
    # END OF SOLUTION


def check(candidate):

    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured
    candidate([], 0)
    sys.stdout = sys.__stdout__
    # get the stdout from the captured output
    captured_output = captured.getvalue()
    assert captured_output.strip().replace(" ", "") == "my_func"


if __name__ == "__main__":
    check(my_func)