"""
Q.4) Write a Python function interval_intersect that takes the parameter a,b,c and d
and returns True if the intervals [a,b] and [c,d] intersects and False otherwise.
"""

a = int(input("Enter value 'a': "))
b = int(input("Enter value 'b': "))
c = int(input("Enter value 'c': "))
d = int(input("Enter value 'd': "))


def interval_intersect(a, b, c, d):
    if a > d or b < c:
        return False
    else:
        return True


result = interval_intersect(a, b, c, d)
print(result)
