"""
BISECTION METHOD (Ref: http://mathworld.wolfram.com/Bisection.html)
Bisection method is a method to find root by bisecting a given interval and selecting
a root with the subintervals which will be further processed.

The program already has the function f(x) = ((x**5) - (5*(x**4)) + (8*(x**3)) - (5*(x**2)) + (11*x) - 7)
in desiredFunction for computation but that can be changed based on user's needs.
Once the intervals and error tolerance are supplied, the program calculates the root.
"""
import math

def desiredFunction(x):
    """ Computes the value of the given equation at given point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the given equation at given point x

    """
    return float((x**5) - (5*(x**4)) + (8*(x**3)) - (5*(x**2)) + (11*x) - 7)


#### MAIN PROGRAM ####

print '""""'
print 'BISECTION METHOD FOR FINDING ROOT'
print '""""'
print ''

#User input for intervals, error tolerance
print("Enter the interval [a,b]")
start_point = int(input("Start point (a) = "))
end_point = int(input("End point (b) = "))
print("The tolerance is in form of 10^(-n). Enter n.")
error_tol = int(input())

divide = math.log10(2)
number = math.log10(end_point - start_point)
# Maximum number of iteration is calculated inorder to find root that lie within supplied error bound
NoOfIteration = round((error_tol + number )/ (divide))

value_A = float(desiredFunction(start_point))
value_B = float(desiredFunction(end_point))
midpoint = float((start_point + end_point)/2)
#print 'First midpoint' + str(midpoint)
value_mid = float(desiredFunction(midpoint))

#Assigning value to iteration
iteration = 1

while iteration <= NoOfIteration:
    if value_mid == 0:
        break
    else:
        if value_A*value_mid < 0:
            start_point = start_point
            end_point = midpoint

        else:
            start_point = midpoint
            end_point = end_point

    iteration += 1
    value_A = float(desiredFunction(start_point))
    value_B = float(desiredFunction(end_point))
    midpoint = float((start_point + end_point)/2)
    value_mid = float(desiredFunction(midpoint))

print 'Here is the root of the the desired function at interval [a,b]: ' + str(midpoint)
