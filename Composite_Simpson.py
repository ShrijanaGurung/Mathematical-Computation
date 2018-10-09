"""
Composite Simpson's rule is a method of numerical integration.
This program follows the composite simpson's rule to find the numerical approximation
of a function (f(x)) in a given definite interval.
Here, f(x) = (2/(1+x**3)).
For different function approximation, the equation in the desired_function can be changed.
"""

def desiredFunction(x):
    """ Computes the value of the given equation at given point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the given equation at given point x

    """
    return 2/(1+x**3)

def computingH(start,end,total):
    """ Computes the h value i.e. the width of the subintervals.
    Args:
        start: The start point of given interval
        end: The end point of gvien interval
        total: Total number of sub intervals by which the given interval
        [start, end] is divided equally.

    Returns:
        The equal width of the each subintervals
    """
    
    return float((end - start)/total)

#### MAIN PROGRAM ####

print '""""'
print 'COMPOSITE SIMPSON RULE FOR NUMERICAL APPROXIMATION'
print '""""'
print ''

#User input for intervals, number of subdivisions
print 'Please enter your intervals (start point and end point) and desired no. of sub intervals.'
start_point = input("Start point (a) = ")
end_point = input("End point (b) such that (b > a) = ")
total_subdivision = int(input("Enter the total number of subintervals. "))

start_point = float(start_point)
end_point = float(end_point)
h = computingH(start_point,end_point,total_subdivision) #width of the subintervals
print '\n'
print 'The width of the subintervals: ' + str(h) +' \n'
####Value at the endpoints of the interval####
ValueAtA = desiredFunction(start_point)
print 'Value at start point: ' + str(ValueAtA)
ValueAtB = desiredFunction(end_point)
print 'Value at end point:' + str(ValueAtB) + '\n'

"""
First sum computation for the approximation:
Given,
n = total_subdivision
f(x) = desired_function(x)
h = width of the subintervals
a = start point

Calculate:
2f(x_2j) where x_j = a + (j*h)
Interval for j = 1 to ((n/2) -1)
"""
first_computation = 0
point = (total_subdivision/2)
for i in range(1,int(point)):
    number = 2* i
    xValue = start_point + (number * h)
    yValue = desiredFunction(xValue)
    first_computation += yValue

sumOne = 2 * first_computation

"""
Second sum computation for the approximation:
Given,
n = total_subdivision
f(x) = desired_function(x)
h = width of the subintervals
a = start point

Calculate:
4f(x_(2j - 1)) where x_j = a + (j*h)
Interval for j = 1 to n/2
"""
second_computation = 0
for i in range(1,int((total_subdivision/2)+ 1)):
    number = (2*i) - 1
    xValue = start_point + (number * h)
    yValue = desiredFunction(xValue)
    second_computation += yValue

sumTwo = 4 * second_computation

"""
Inorder to get the numerical approximation, we add the f(x) value at the start and
end of the interval and the first and second sum computation.
Then, the total is multiplied by (h/3).
"""
total = ValueAtA + ValueAtB + sumOne + sumTwo
final_approximation = (h/3) * total
print 'The numerical approximation of f(x) in given interval is: ' + str(final_approximation)
    
