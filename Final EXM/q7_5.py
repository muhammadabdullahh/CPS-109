#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Recursion: is there a repeated value in the list
# --------------------------------------------------------------
def repeat(L) :
    '''
    Assume that L is a list of integers.
    Return True if some value in L occurs more than once.

    For example, 
    repeat([5, 2, 5, 3]) returns True
    repeat([5, 2, 9, 3]) returns False

    CONSTRAINT: YOU MUST USE RECURSION. NO LOOPS. (MARK FOR LOOP IS 0).
    '''
    if len(L) <= 1:
        return False
    if L[0] == L[1]:
        return True
    if repeat(L[2:] + [L[0]]):
        return True
    if repeat(L[1:]):
        return True
    return False

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(repeat([]), False)
 def test2(self):
  self.assertEqual(repeat([5]), False)
 def test3(self):
  self.assertEqual(repeat([144, 5, 2, 9, 80]), False)
 def test4(self):
  self.assertEqual(repeat([144, 5, 2, 9, 5]), True)
 def test5(self):
  self.assertEqual(repeat([1, 2, 3, 4, 5, 1]), True)
 def test6(self):
  self.assertEqual(repeat([1, 1]), True)

if __name__ == '__main__':
 unittest.main(exit=True)




# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
