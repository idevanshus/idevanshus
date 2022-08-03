"""
Q.2) Ask the user to input a positive integer and print whether it is even or odd.
Also, check if the input given by the user is appropriate i.e. the number is not
a positive integer.
"""

a = int(input("Enter a number: "))
if a > 0:
    mod_a = a % 2
    if mod_a > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")
else:
    print("Please enter only positive values")
