"""Functions checking types of triangles"""
def is_triangle(sides):
    a , b , c = sorted(sides)
    return a > 0 and a + b >= c    
def equilateral(sides):
    """Function checking equilateral triangles"""
    return is_triangle(sides) and len(set(sides)) == 1 
def isosceles(sides):
    """Functons checking isosceles triangles"""
    return is_triangle(sides) and len(set(sides)) <= 2
def scalene(sides):
    """Function checking scalene triangles"""
    return is_triangle(sides) and len(set(sides)) == 3   
