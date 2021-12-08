#!/usr/bin/python3
import unittest


# --------------------------------------------------------------
def find_root4(x, epsilon):
    '''
    Assume: x, epsilon are floating point numbers and epsilon > 0
    Use bisection search to find the following root of x such that
    If x >=0, return y such that x - epsilon <= y ** 2 <= x + epsilon
    Else, return y such that x - epsilon <= y ** 7 <= x + epsilon

    Note: You must use bisection search to implement the function.
    '''
    # YOUR CODE GOES HERE
    y = 1
    while abs(x - y ** 2) >= epsilon:
        y = (y + x / y) / 2
    return y


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        x, epsilon = 0.0, 0.0001
        y = find_root4(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 2 - x)
        self.assertTrue(error <= epsilon)

    def test2(self):
        x, epsilon = -50.0, 0.001
        y = find_root4(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 7 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)

    def test3(self):
        x, epsilon = -0.5, 0.001
        y = find_root4(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 7 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)

    def test4(self):
        x, epsilon = 2.0, 0.001
        y = find_root4(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 2 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)

    def test5(self):
        x, epsilon = 0.3, 0.001
        y = find_root4(x, epsilon)
        if y == None:
            error = 10*epsilon
        else:
            error = abs(y ** 2 - x)
        self.assertTrue(error <= epsilon)
        self.assertFalse(error <= epsilon / 100)


if __name__ == '__main__':
    unittest.main(exit=True)

# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
