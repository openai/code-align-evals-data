def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    
    Example solution:
    # line 1
    letter_grade = []
    # line 2
    for gpa in grades:
        # line 3
        if gpa == 4.0:
            # line 4
            letter_grade.append("A+")
        # line 5
        elif gpa > 3.7:
            # line 6
            letter_grade.append("A")
        # line 7
        elif gpa > 3.3:
            # line 8
            letter_grade.append("A-")
        # line 9
        elif gpa > 3.0:
            # line 10
            letter_grade.append("B+")
        # line 11
        elif gpa > 2.9:
            # line 12
            letter_grade.append("B")
        # line 13
        elif gpa > 2.3:
            # line 14
            letter_grade.append("B-")
        # line 15
        elif gpa > 2.0:
            # line 16
            letter_grade.append("C+")
        # line 17
        elif gpa > 1.7:
            # line 18
            letter_grade.append("C")
        # line 19
        elif gpa > 1.3:
            # line 20
            letter_grade.append("C-")
        # line 21
        elif gpa > 1.0:
            # line 22
            letter_grade.append("D+")
        # line 23
        elif gpa > 0.7:
            # line 24
            letter_grade.append("D")
        # line 25
        elif gpa > 0.0:
            # line 26
            letter_grade.append("D-")
        # line 27
        else:
            # line 28
            letter_grade.append("E")
    # line 29
    return letter_grade
    
    """
    # Please print out which line of the above program contains an error. E.g. if the bug is on line 4 then print 4
    # END OF CONTEXT
    print("11")
    # END OF SOLUTION

def check(candidate):

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        candidate([])
    out = f.getvalue().strip('\n')

    assert "11" == out
    for i in range(0, 35):
        if i != 11:
            assert str(i) != out

if __name__ == '__main__':
    check(numerical_letter_grade)
