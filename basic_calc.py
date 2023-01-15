"""
This example illustrates Python expressions -
a type of statement that returns a value.

Statements
----------

Some statements perform an action, like printing a value to the screen.

Some statements are expressions, which return a value.

Expressions
-----------

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
"""
print()
print("Greetings!")
print()

# let's do some math and show off our skills
triangle_base = 10
triangle_height = 5
triangle_area = triangle_base * triangle_height / 2

print("With scripts, ")
print("It's import to print() everything the user should see.")
print("We could concatenate text like before, but there's a better way.")
print()
print(f"Given base={triangle_base} and height={triangle_height},")
print(f"the area of a triangle is {triangle_area}")
print()
print("Python provides formatted strings called f-strings")
print("for combining text and values. ")
print("We don't have to call str() anymore")
print()
print("Look at the code. Find the f that makes it an fstring.")
print()
print("Add logic to calculate the area of a rectangular plot of land.")
print("Display the results to the user.")
print()
rectangle_width = 5000
rectangle_length = 5000
rectangle_area = rectangle_width * rectangle_length

print("I am going to buy a rectangular plot of land. Let's do some math to determine its area!")
print(f"The plot width is {rectangle_width} feet and the plot length is {rectangle_length} feet,") 
print(f"thus the area of my plot of land is {rectangle_area} square feet!")