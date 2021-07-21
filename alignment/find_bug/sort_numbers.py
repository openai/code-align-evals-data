from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    
    Example solution:
    # line 1
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # line 2
    ret = []
    # line 3
    for x in numbers.split():
        # line 4
        ret.append([x, value_map[x]])
    # line 5
    ret.sort(key=lambda x: x[1])
    # line 6
    ret = [x for x, y in ret]
    # line 7
    ret = '  '.join(ret)
    # line 8
    return ret
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("7")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 10):
        if i != 7:
            assert str(i) != out

if __name__ == '__main__':
    check(sort_numbers)
