"""
Composite Trapezoid is approximation method to find area under a curve y = f(x).
This program follows the composite trapezoid's rule to find the area under the curve
y = f(x) = (2/(1 + x **3)).
For different function approximation, the equation in the desired_function can be changed.

Additionally, the error tolerance is also observed to get a better approximation value.
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
print 'COMPOSITE TRAPEZOID RULE FOR NUMERICAL APPROXIMATION'
print '""""'
print ''

###User input for intervals ####
print 'Please enter your intervals (start point and end point), desired number of sub interval and error tolerance.'
start_point = float(input("Start point (a) = "))
end_point = float(input("End point (b) such that (b > a) = "))
total_subdivision = int(input("Enter the total number of subintervals. "))
error_tol = float(input("Enter your error tolerance."))

####Value at the endpoints of the interval####
ValueAtA = desiredFunction(start_point)
print 'Value at a: ' + str(ValueAtA)
ValueAtB = desiredFunction(end_point)
print 'Value at b: ' + str(ValueAtB)

h = computingH(start_point,end_point,total_subdivision) #width of the subintervals
#Check if the given n gives us value within our error tolerance limit
secPoint = start_point + h
secValue = desiredFunction(secPoint)

while abs(secValue - ValueAtA) >  error_tol:
    print("The given number of subintervals doesn't meet our error tolerance requirement. Please choose a different total.")
    total_subdivision = int(input())
    h = computingH(a,b,n) #compute new h based on new total
    secPoint = start_point + h
    secValue = desiredFunction(secPoint)
    
print '\n'
print 'The width of the subintervals: ' + str(h) +' \n'


"""
Sum computation for the approximation:
n = total_subdivision
f(x) = desired_function(x)
h = width of the subintervals
a = start point

Calculate:
f(x_(k - )1) + f(x_k) where x_k = a + kh
Interval for k = 1 to n

"""
sumWithinInterval = 0
for i in range(1,total_subdivision):
    xValue = start_point + (i*h)
    yValue = desiredFunction(xValue)
    sumWithinInterval = sumWithinInterval + yValue

totalSum = ValueAtA + ValueAtB + 2*sumWithinInterval
final_approximation = (h/2)*(totalSum)

print 'The numerical approximation of f(x) in given interval is: ' + str(final_approximation)
