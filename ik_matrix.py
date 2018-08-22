from sympy import *

theta = symbols('theta')


T01 = Matrix([[cos(theta), sin(theta), 0, 0], 
              [-sin(theta), cos(theta), 0, 0], 
              [0, 0, 1, 0],  
              [0, 0, 0, 1]
              ])
print(T01)