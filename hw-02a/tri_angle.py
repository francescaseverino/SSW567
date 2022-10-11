# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a_length,b_length,c_length):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a_length,int) and isinstance(b_length,int) and isinstance(c_length,int)):
        return 'InvalidInput'

    # require that the input values be >= 0 and <= 200
    if a_length > 200 or b_length > 200 or c_length > 200:
        return 'InvalidInput'

    if a_length <= 0 or b_length <= 0 or c_length <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a_length >= (b_length + c_length)) or (b_length >= (a_length + c_length)) \
        or (c_length >= (a_length + b_length)):
        return 'NotATriangle'

    triangle = 'Isoceles'

    # now we know that we have a valid triangle
    if a_length == b_length and b_length == c_length:
        triangle = 'Equilateral'
    elif ((a_length * a_length) + (b_length * b_length)) == (c_length * c_length):
        triangle = 'Right'
    elif (a_length != b_length) and  (b_length != c_length) and (a_length != c_length):
        triangle = 'Scalene'
    return triangle
