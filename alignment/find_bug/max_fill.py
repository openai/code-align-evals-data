def max_fill(grid, capacity):
    """
    Given a rectangular grid representing wells, every column is a one well,
    and 1 means "water exists", 0 means no water,
    and you have a bucket, and know its capacity,
    your task is to use the bucket to empty the wells,
    the output will be the number of times that you filled the bucket.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    
    Example solution:
    # line 1
    import math
    # line 2
    grid_sum = 0
    # line 3
    for i in range(len(grid)):
        # line 4
        row_sum = 0
        # line 5
        for j in range(len(grid[i])):
            # line 6
            row_sum += grid[i][j]
        # line 7
        grid_sum += row_sum / capacity
    # line 8
    return grid_sum
    
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
        candidate([], 1)
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 10):
        if i != 7:
            assert str(i) != out

if __name__ == '__main__':
    check(max_fill)
