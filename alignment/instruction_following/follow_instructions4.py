def my_func():
    # Please print a number that is divisible by 7
    # END OF CONTEXT
    print(14)
    # END OF SOLUTION


def check(candidate):
    import io
    import sys

    captured = io.StringIO()
    sys.stdout = captured
    candidate()
    sys.stdout = sys.__stdout__

    # get the stdout from the captured output
    captured_output = captured.getvalue()
    assert int(captured_output) % 7 == 0, "Not divisible by 7"


if __name__ == "__main__":
    check(my_func)