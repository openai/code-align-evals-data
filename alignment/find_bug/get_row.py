def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    it may have different number of columns and rows.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    
    Example solution:
    # line 1
    coords = []
    # line 2
    for i in range(len(lst)):
        # line 3
        for j in range(len(lst[i])):
            # line 4
            if lst[i][j] == x:
                # line 5
                coords.append((i, j))
    # line 6
    return sorted(sorted(coords, key=lambda x: x[1]), key=lambda x: x[0])
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("6")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([], 0)
    out = f.getvalue().strip('\n')

    assert "6" == out
    for i in range(0, 10):
        if i != 6:
            assert str(i) != out

if __name__ == '__main__':
    check(get_row)
