#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
# Pay with Overtime. 
# --------------------------------------------------------------
def calcWeeklyWages(totalHours, hourlyWage):
    '''
    Assume that totalHours is the person’s work hours for the week 
    Assume that hourly wage is the regular hourly wage for <= 40 hours
    Assume that the overtime hourly wage is 1.5 times the normal rate
    and that the overtime rate is applied to time in excess of 40 hours.
    Return the total pay for the week.
    For example, 
    calcWeeklyWages(40, 15) returns 600.0, since 40h * 15/hour
    calcWeeklyWages(100, 15) returns 1950.0, since 40 * 15 + 60 * 1.5 * 15
    '''
    total = 0
    overtimeWage = hourlyWage * 1.5
    overtime = totalHours - 40
    if overtime > 0:
          total += (overtime * overtimeWage)
          remaining = totalHours - overtime
          total += (hourlyWage * remaining)
    else:
          total = hourlyWage*totalHours
    return total
          
    
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
 def test1(self):
  self.assertEqual(calcWeeklyWages(40, 15), 600)
 def test2(self):
  self.assertEqual(calcWeeklyWages(0, 15), 0)
 def test3(self):
  self.assertEqual(calcWeeklyWages(100, 15), 1950.0)
 def test4(self):
  self.assertEqual(calcWeeklyWages(1, 15), 15)
 def test5(self):
  self.assertEqual(calcWeeklyWages(58, 15), 1005.0)


if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
