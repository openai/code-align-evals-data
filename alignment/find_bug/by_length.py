def by_length(arr):
    """
    Given an array of integers, if the number is an integer between 1 and 9 inclusive,
    replace it by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    otherwise remove it, then sort the array and return a reverse of sorted array.

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    
    Example solution:
    # line 1
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    # line 2
    sorted_arr = sorted(arr, reverse=True)
    # line 3
    sorted_arr.reverse()
    # line 4
    new_arr = []
    # line 5
    for var in sorted_arr:
        # line 6
        try:
            # line 7
            new_arr.append(dic[var])
        # line 8
        except:
            # line 9
            pass
    # line 10
    return new_arr
    """
    
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("2")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "2" == out
    for i in range(0, 15):
        if i != 2:
            assert str(i) != out

if __name__ == '__main__':
    check(by_length)
