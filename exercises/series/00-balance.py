# Complete the following function. It should return the number of characters in the string `s`
# Example 1: `count_chars('')` returns 0
# Example 2: `count_chars('a')` returns 1
# Example 3: `count_chars('hello')` returns 5
def count_chars(s):
    pass

# Do not modify the test cases below
assert count_chars('') == 0
assert count_chars('a') == 1
assert count_chars('hello') == 5
assert count_chars('abc' * 5) == 15

# Complete the following function. It should return the number of `c` characters in the string `s`
# Example 1: `count_matches('a', '')` returns 0
# Example 2: `count_matches('a', 'bc')` returns 0
# Example 3: `count_matches('a', 'aaa')` returns 3
# Example 4: `count_matches('e', 'hello')` returns 1
# Example 5: `count_matches('a', 'alphabet')` returns 2
def count_matches(c, s):
    pass

# Do not modify the test cases below
assert count_matches('a', '') == 0
assert count_matches('a', 'bc') == 0
assert count_matches('a', 'aaa') == 3
assert count_matches('e', 'hello') == 1
assert count_matches('a', 'alphabet') == 2

# Complete the following function. It should return the number of characters before the first `c` character in the string `s`
# Example 1: `count_before('a', '')` returns 0
# Example 2: `count_before('a', 'a')` returns 0
# Example 3: `count_before('a', 'ab')` returns 0
# Example 4: `count_before('b', 'ab')` returns 1
# Example 5: `count_before('w', 'hello, world!')` returns 7
def count_before(c, s):
    pass

# Do not modify the test cases below
assert count_before('a', '') == 0
assert count_before('a', 'a') == 0
assert count_before('a', 'ab') == 0
assert count_before('b', 'ab') == 1
assert count_before('b', 'hello, world!') == 7

# Complete the following function. It should return `true` if parentheses in `s` are balanced, and `false` otherwise
# Parenthesis are balanced if every open-parenthesis has a closing parenthesis
# E.g.
#   '' is balanced because it has no parentheses
#   '()' is balanced because the first parenthesis is closed by the last parenthesis
#   '(' is not balanced because the first parenthesis is never closed
#   ')' is not balanced because the first parenthesis doesn't close a prior open-parenthesis
#   ')(' is not balanced because the first parenthesis doesn't close a prior open-parenthesis
#   '()()' is balanced because each open-parenthesis has a corresponding close-parenthesis
#   '(())' is balanced because each open-parenthesis has a corresponding close-parenthesis
#   '(()))' is not balanced because each one more parenthesis is closed than opened
#   '((())' is not balanced because each one more parenthesis is opened than closed
#
# Example 1: `is_balanced('')` returns true
# Example 2: `is_balanced('()')` returns true
# Example 3: `is_balanced('(')` returns false
# Example 4: `is_balanced(')')` returns false
# Example 5: `is_balanced(')(')` returns false
# Example 6: `is_balanced('()()')` returns true
# Example 7: `is_balanced('(())')` returns true
def is_balanced(s):
    pass

assert is_balanced('')
assert is_balanced('()')
assert not is_balanced('(')
assert not is_balanced(')')
assert not is_balanced(')(')
assert is_balanced('()()')
assert is_balanced('(())')
assert not is_balanced('(()))')
assert not is_balanced('((())')
