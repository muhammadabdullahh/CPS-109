import unittest
"""
2D arrays

You are given an array A1 of size x rows, y columns, 
a second array A2 of size y rows and z columns,
as well as a row index i1 and a column index i2.

Multiply the first element of the row index i1 from A1 and 
the first element of the column index i2 from A2. 
Likewise for the 2nd, 3rd, Nth elements, 
and finally sum up the results.

Example 1:
A1 = [[1, 2, 3], [4, 5, 6]]
A2 = [[7, 8, 9], [10, 11, 12], [13, 14, 15]] 
i1 = 0 
i2 = 2
result = 1*9 + 2*12 + 3*15 = 78, so 
multiply(A1, A2, i1, i2) returns 78

Example 2:
A1 = [[10, 3], [44, 15]]
A2 = [[14, 28], [1,6]] 
i1 = 1 
i2 = 0
result = 44*14 + 15*1 = 631, so 
multiply(A1, A2, i1, i2) returns 631
"""

# --------------------------------------------------------------
# Your implementation: 
# --------------------------------------------------------------
def multiply(a1,a2,i1,i2):
    #i1 is row, from A1
    #i2 is coloumb from A2
    sum = 0
    for i in range(len(a1[i1])):
        sum += a1[i1][i] * a2[i][i2]
    return sum

# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
  def test1(self):
      A1 = [[1, 2, 3], [4, 5, 6]]
      A2 = [[7, 8, 9], [10, 11, 12], [13, 14, 15]] 
      self.assertEqual(multiply(A1, A2, 0, 2), 78)
  def test2(self):
      A1 = [[10, 3], [44, 15]]
      A2 = [[14, 28], [1,6]] 
      self.assertEqual(multiply(A1, A2, 1, 0), 631)
  def test3(self):
      A1 = [[1, 1, 1, 1], [2, 2, 2, 2], [7, 7, 7, 7]]
      A2 = [[4, 3], [17, 68], [45, 33], [12, 11]] 
      self.assertEqual(multiply(A1, A2, 2, 1), 805)
          
if __name__ == '__main__':
  unittest.main(exit=True)
 
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
