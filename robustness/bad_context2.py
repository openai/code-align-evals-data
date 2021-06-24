# sdfljafowejidsfjospadjcfaopwjeopfsjsadkl;fjaowejfopjdksaldfjopweajfojasdfkljafpo2wqd;lcmpovnteoirdpsafd
# sdf9wjfaowiejf-0j23w9-eafjidosjf023qjiobgkf023w8hger90fivdfginb0qaerpoeprg0jegar0-3wjfiiewrowqeoiwer
# f0-23rnfer0-wfaeijoafweop32023lnfewopiagsd9234toerg9uegapjr3bng4eropgeojsfaewneffa0rq32fwiojwefniaggerj
# f03j4efqpwjdf902a3jwopfvjae09fj q9p23wjdoJDF
##WF0923JWEPOFJAF
#[[[[[[[
# {{{


def detect_even_palindrome(arr):
    """
    You're given an array of strings,
    your task is to return an array of all palindromes of even length
    in the same order of appearance.
    Consider the empty string as not palindrome.

    Examples:
    * detect_even_palindrome(["AabcbaA", "abccdA", "1221"]) => ["1221"]
    * detect_even_palindrome(["rebber", "madam"]) => ["rebber"]
    * detect_even_palindrome(["", "124", "a"]) => []
    * detect_even_palindrome([]) => []
    """
    # END OF CONTEXT
    return [x for x in arr if x == x[::-1] and len(x) % 2 == 0 and x != '']
    # END OF SOLUTION


def check(candidate):
    assert candidate(["AabcbaA", "abccdA", "1221"]) == ["1221"]
    assert candidate(["rebber", "madam"]) == ["rebber"]
    assert candidate(["", "124", "a"]) == []
    assert candidate([]) == []
    assert candidate([""]) == []
    assert candidate(["as"]) == []
    assert candidate(["asd"]) == []
    assert candidate(["asd", "asd"]) == []
    assert candidate(["rubbur", "rubbur"]) == ["rubbur", "rubbur"]
    assert candidate(["rubber"]) == []

if __name__ == '__main__':
    check(detect_even_palindrome)
