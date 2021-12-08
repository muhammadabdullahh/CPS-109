#!/usr/bin/python3
import unittest


def func4(lis):
    '''
    Assume lis is a list of integers and characters.
    Return (num, i) where num is the last integer in the list 
    and i is the index of the last integer.
    Note 1: you may use isinstance(d, int) or isinstance(d, str) 
    to check the type of d
    Note 2: index i should be nonnegative (do not use negtive index)

    For example, lis = ['e', 6, 5, 'f'] should return (5, 2)
    '''
    # YOUR CODE GOES HERE
    for e in range(len(lis)):
        if isinstance(lis[e], int):
            num = lis[e]
            i = e
    return (num, i)
    



# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(func4([1, 2, 3, 'a', 'b', 'c']), (3, 2))

    def test2(self):
        self.assertEqual(func4(['f', 'b', 'c', 2, 3, 6]), (6, 5))

    def test3(self):
        self.assertEqual(func4(['d', 3, 2, 'b', 'c', 3]), (3, 5))

    def test4(self):
        self.assertEqual(func4([3, 2, 5, 3, 'c', 'b']), (3, 3))

    def test5(self):
        self.assertEqual(func4(['f', 'b', 4, 1, 'd']), (1, 3))


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
