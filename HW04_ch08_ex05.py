# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

def rotate_word(string, number):
    rotated_word = ''
    for char in string:
        ascii_val = ord(char)
        new_ascii_val = ascii_val + number
        new_char = chr(new_ascii_val)
        rotated_word = rotated_word + new_char
    return rotated_word

rotate_word('bugaboo', 1)
