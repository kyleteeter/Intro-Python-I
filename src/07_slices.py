"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
y= a[1:2]
print(y)

# Output the second-to-last element: 9
x= a[4:5]
print(x)

# Output the last three elements in the array: [7, 9, 6]
z = a[3:]
print(z)

# Output the two middle elements in the array: [1, 7]
w = a[2:4]
print(w)

# Output every element except the first one: [4, 1, 7, 9, 6]
r = a[1:]
print(r)

# Output every element except the last one: [2, 4, 1, 7, 9]
t = a[:5]
print(t)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
v = s[7:12]
print(v)