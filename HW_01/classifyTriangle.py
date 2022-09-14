import math
import unittest

def classify_triangle(a, b, c):

    if(a < 1 or b < 1 or c < 1):            # all lengths must be greater than zero
        return "Invalid Triangle Parameters"

    if(a + b <= c or b + c <= a or a + c <= b): # the sum of 2 sides must be greater than the third side
        return "Invalid Triangle Parameters"

    triangleType = ""
    isRightTri = False
    
    if(a == b and b == c):              # if all sides are the same -> Equalateral != Right Triangle
        return 'Equalateral Triangle'
    elif(a == b or b == c or a == c):   # if two sides are the same
        triangleType = 'Isosceles '
    else:                               # if none of the sides are the same
        triangleType = 'Scalene '

    if(round(a**2) + round(b**2) == round(c**2)): # a^2 + b^2 = c^2
        isRightTri = True;
        
    return triangleType + 'Right Triangle' if isRightTri == True else triangleType + 'Triangle'


class TestTriangles(unittest.TestCase):

    def testValidity(self): #testing for the validity of the triangles
        self.assertEqual(classify_triangle(2, 7, 10), 'Invalid Triangle Parameters', 'classify_triangle(2, 7, 10) should be an Invalid Triangle Parameters')
        self.assertEqual(classify_triangle(-1, 4, 10), 'Invalid Triangle Parameters', 'classify_triangle(-1, 4, 10) should be an Invalid Triangle Parameters')
        self.assertEqual(classify_triangle(2, 3, 0), 'Invalid Triangle Parameters', 'classify_triangle(2, 3, 0) should be an Invalid Triangle Parameters')
        self.assertEqual(classify_triangle(1, 2, 3), 'Invalid Triangle Parameters', 'classify_triangle(1, 2, 3) should be an Invalid Triangle Parameters')
        
    def testInputs(self): #testing the various different inputs
        self.assertEqual(classify_triangle(3, 3, 3), 'Equalateral Triangle', 'classify_triangle(3, 3, 3) should be an Equalateral Triangle')
        self.assertEqual(classify_triangle(4, 4, 4), 'Equalateral Triangle', 'classify_triangle(4, 4, 4) should be an Equalateral Triangle')
        self.assertEqual(classify_triangle(14, 14, 14), 'Equalateral Triangle', 'classify_triangle(4, 4, 4) should be an Equalateral Triangle')
        
        self.assertEqual(classify_triangle(3, 4, 5), 'Scalene Right Triangle', 'classify_triangle(3, 4, 5) should be a Scalene Right Triangle')
        self.assertEqual(classify_triangle(math.sqrt(3), 1, 2), 'Scalene Right Triangle', 'classify_triangle(math.sqrt(3), 1, 2) should be a Scalene Right Triangle')
        self.assertEqual(classify_triangle(2, 6.5, 7), 'Scalene Triangle', 'classify_triangle(2, 6.5, 7) should be a Scalene Triangle')

        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), 'Isosceles Right Triangle', 'classify_triangle(1, 1, math.sqrt(2) should be an Isosceles Right Triangle')
        self.assertEqual(classify_triangle(3, 3, 2), 'Isosceles Triangle', 'classify_triangle(3, 3, 2) should be an Isosceles Triangle')
        self.assertEqual(classify_triangle(14, 14, 4), 'Isosceles Triangle', 'classify_triangle(14, 14, 4) should be an Isosceles Triangle')

if __name__ == '__main__':
    
    print('Running unit tests')
    unittest.main(exit=False)
