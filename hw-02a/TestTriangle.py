# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from tri_angle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleScalene(self): 
        self.assertEqual(classify_triangle(8,6,10),'Right','classifyTriangle(8,6,10) is a Scalene Right triangle')

    def testScalene(self):
        self.assertEqual(classify_triangle(5,6,7),'Scalene','classifyTriangle(5,6,7) is a Scalene triangle')
    
    def testIsosceles(self):
        self.assertEqual(classify_triangle(4,4,5),'Isoceles','classifyTriangle(4,4,5) is a Isosceles triangle')

    def testEquilateralTriangle(self):
        self.assertEqual(classify_triangle(3,3,3),'Equilateral','classifyTriangle(3,3,3) is a Equilateral triangle')

    def testInvalidTriangle(self):
        self.assertEqual(classify_triangle(7,2,10),'NotATriangle','classifyTriangle(7,2,10) is not a triangle.')

    def testInvalidInput_1(self):
        self.assertEqual(classify_triangle(-7,2,10),'InvalidInput','classifyTriangle(-7,2,10) is a invalid input.')

    def testInvalidInput_2(self):
        self.assertEqual(classify_triangle(3,"4","5"),'InvalidInput','classifyTriangle(3,"4","5") is a invalid input.')
    
    def testInvalidInput_3(self):
        self.assertEqual(classify_triangle(13.5,14.5,15),'InvalidInput','classifyTriangle(13.5,14.5,15) is a invalid input.')

    # added in part 2
    def testInvalidInput_4(self):
        self.assertEqual(classify_triangle(0,1,1),'InvalidInput','classifyTriangle(0,1,1) is a invalid input.')
    
    def testInvalidInput_5(self):
        self.assertEqual(classify_triangle(201,150,180),'InvalidInput','classifyTriangle(200,150,180) is a invalid input.')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

