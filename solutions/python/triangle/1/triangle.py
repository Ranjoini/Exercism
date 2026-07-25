"""Functions checking types of triangles"""
def is_triangle(sides):
    a , b , c = sorted(sides)
    return a > 0 and a + b >= c    
def equilateral(sides):
    a , b , c = (sides)
    return is_triangle(sides) and (a == b == c) 
def isosceles(sides):
    a , b , c = (sides)
    return is_triangle(sides) and (a == b or b == c or a == c)
def scalene(sides):
    a , b , c = (sides)
    return is_triangle(sides) and (a != b and b!= c and a != c)    
