"""
Q.1) Write a program to calculate the Euclidean Distance between (2,3) and (2,5).
"""

# Assigning (x1,y1) and (x2,y2) two points in the space as (2,3) and (2,5)

x1 = 2
y1 = 3

x2 = 2
y2 = 5

"""Using Euclidean Distance formula to calculate distance between these two points,
   Euclidean Distance = d = √[(x2 – x1)^2 + (y2 – y1)^2]"""

result = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

print("Euclidean Distance between", (x1, y1), "and", (x2, y2), "is : ", result)
