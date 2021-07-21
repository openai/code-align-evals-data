def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of the days not less or higher than 31 days for months 1,3,5,7,8,10,12.And the number of days not less than or higher 30 days for months 4,6,9,11. And, the number of days not less 28 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    
    Example solution:
    # line 1
    try:
        # line 2
        date = date.strip()
        # line 3
        month, day, year = date.split('-')
        # line 4
        month, day, year = int(month), int(day), int(year)
        # line 5
        if month < 1 or month > 12:
            # line 6
            return False
        # line 7
        if month in [1,3,5,6,8,10,12] and day < 1 or day > 31:
            # line 8
            return False
        # line 9
        if month in [4,6,9,11] and day < 1 or day > 30:
            # line 10
            return False
        # line 11
        if month == 2 and day < 1 or day > 29:
            # line 12
            return False
    # line 13
    except:
        # line 14
        return False
    # line 15
    return True
    
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
        candidate('')
    out = f.getvalue().strip('\n')

    assert "7" == out
    for i in range(0, 20):
        if i != 7:
            assert str(i) != out

if __name__ == '__main__':
    check(valid_date)
