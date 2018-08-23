from sympy import *

theta1 = symbols('theta1')
theta2 = symbols('theta2')
theta3 = symbols('theta3')
l1 = symbols('l1')
l2 = symbols('l2')
l3 = symbols('l3')
fi = symbols('fi')
x = symbols('x')
y = symbols('y')
z = symbols('z')

T01 = Matrix([[cos(theta1), -sin(theta1), 0, 0], 
              [sin(theta1), cos(theta1), 0, 0], 
              [0, 0, 1, 0],  
              [0, 0, 0, 1]
              ])

T12 = Matrix([[cos(theta2), -sin(theta2), 0, l1], 
              [sin(theta2), cos(theta2), 0, 0], 
              [0, 0, 1, 0],  
              [0, 0, 0, 1]
              ])

T23 = Matrix([[cos(theta3), -sin(theta3), 0, l2], 
              [sin(theta3), cos(theta3), 0, 0], 
              [0, 0, 1, 0],  
              [0, 0, 0, 1]
              ])

T3w = Matrix([[1, 0, 0, l3], 
              [0, 1, 0, 0], 
              [0, 0, 1, 0],  
              [0, 0, 0, 1]
              ])


print('##### T02 = T01 * T12 ######')
T02 = T01 * T12
print(T02)
print('##### T03 = T02 * T23 ######')
T03 = T02 * T23
print(T03)
print('##### T0W = T03 * T3w ######')
T0w = T03 * T3w
print(T0w)