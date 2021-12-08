#!/usr/bin/python3
import unittest
# --------------------------------------------------------------
class TrafficJam:
    '''
    A TrafficJam is a list of Car and Duck objects.
    The list is called jam_objects.
    The Car and Duck classes are given below and are already 
    fully implemented. Car and Duck objects have a method honk()
    which returns "beep!" for a car and "quack!" for a duck.
    
    Fill in the code below wherever it says "###YOUR CODE GOES HERE"

    For example, the following code:

    jam = TrafficJam()  
    car = Car()
    duck = Duck()
    jam.add_traffic(car)   # jam.jam_objects becomes [car]
    jam.add_traffic(duck)  # jam.jam_objects becomes [car, duck]
    jam.traffic_symphony() # calls honk() on each of the elements of jam_objects

    would return ["quack!", "beep!"].  # the reverse of ["beep!", "quack!"]
    '''
    def __init__(self) :
        '''
        Creates an empty list called jam_objects.
        '''
        ### GIVEN CODE
        self.jam_objects = []

    def add_traffic(self, b) :
        '''
        Assumes that b is a Car object or a Duck object.
        Adds object b to the end of jam_objects list.
        '''
        self.jam_objects.append(b)

    def traffic_symphony(self) :
        '''
        Returns the reverse of a list of strings created by calling 
        e.honk() for each object e in jam_objects.
        '''
        newList = []
        for elem in self.jam_objects:
            newList.append(elem.honk())
        newList.reverse()
        return newList
    
class Car:
    '''
    A Car is an object that returns "beep!" when it's honk() method 
    is called.
    '''
    def __init__(self) :
        pass
    def honk(self) :
        return 'beep!'

class Duck:
    '''
    A Duck is an object that returns "quack!" when it's honk() method 
    is called.
    '''
    def __init__(self) :
        pass
    def honk(self) :
        return 'quack!'
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        t = TrafficJam()
        self.assertEqual(t.jam_objects, [])
    def test2(self):
        t = TrafficJam()
        c = Car()
        t.add_traffic(c)
        self.assertEqual(t.jam_objects, [c])
    def test3(self):
        t = TrafficJam()
        c = Car()
        d = Duck()
        t.add_traffic(c)
        t.add_traffic(d)
        self.assertEqual(t.jam_objects, [c,d])
    def test4(self):
        t = TrafficJam()
        c = Car()
        d = Duck()
        t.add_traffic(c)
        t.add_traffic(d)
        self.assertEqual(t.traffic_symphony(), ["quack!", "beep!"])
    def test5(self):
        t = TrafficJam()
        c = Car()
        c2 = Car()
        d = Duck()
        t.add_traffic(d)
        t.add_traffic(c)
        t.add_traffic(c2)
        self.assertEqual(t.traffic_symphony(), ["beep!", "beep!", "quack!"])
if __name__ == '__main__':
 unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
