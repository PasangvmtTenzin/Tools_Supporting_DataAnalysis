'''Write a program that solves a given quadratic equation. Make sure that your code properly handles all cases (but assume that the user enters - when asked - integers).

Use the if statement. Pay attention to handle all possible cases. This will require nesting if statements (or using more complex conditions). Remember about the elif construct too.

To compute the square root use the sqrt function from the math module. The syntax of calling a function from a module depends on the import statement, we recommend here import math and math.sqrt(...).

Also the int string to integer conversion will be handy (you may use float as well, if you prefer real numbers as coefficients).

Pay attention to the calculation order and proper use of parenthesis.

A simple extension of this program: print out the equation with coefficients. Use the ^2 or **2 notation to describe raising a number to the given power (only the latter works in Python).

Sample output of the program:

The quadratic equation solver (ver. 1.23, July 26th, 2034).
Enter the quadratic coefficient: 1
Enter the linear coefficient: -1
Enter the free term: -6
The equation has two roots: -2 and 3.'''

import math

# Quadratic equation solver v. 1.2 (July 26th, 2034)

# Get coefficients from the user
a = int(input("Enter the quadratic coefficient: "))
b = int(input("Enter the linear coefficient: "))
c = int(input("Enter the free term: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the discriminant to determine the number and nature of roots
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("The equation has two roots:", root1, "and", root2)
elif discriminant == 0:
    # One real and repeated root
    root = -b / (2*a)
    print("The equation has one repeated root:", root)
else:
    # Complex roots
    real_part = -b / (2*a)
    imag_part = math.sqrt(abs(discriminant)) / (2*a)
    root1 = complex(real_part, imag_part)
    root2 = complex(real_part, -imag_part)
    print("The equation has two complex roots:", root1, "and", root2)

# Print the quadratic equation
print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0")
