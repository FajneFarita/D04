#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """returns True when finds the first lowercase letter in a sting, or False
    when doesn't find any. Should work"""
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """'c' in the if-statement is not a variable, but an actual lowercase letter 'c'.
    The return statement will be a string 'True' regardless of the value of the string s.
    (In addition, True and False are not booleans here, but strings)
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Should work
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This code should work. Although, it is not the most straiforward way to do it
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """returns False if the 1st letter is capital. I would remove 'not'
    and replace False with True and True with False.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    any_lowercase1("thisstringmessesupthefunction")
    any_lowercase2("thisstringmessesupthefunction")
    any_lowercase5("thisstringmessesupthefunction")



if __name__ == '__main__':
    main()
