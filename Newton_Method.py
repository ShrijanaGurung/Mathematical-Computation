"""
The program uses newton's method algorithm to find the root for given equation.
Conditions: The function f(x) along with its differentiated equaton is required.
"""

def desiredFuncton(x):
    """ Computes the value of the given equation at given point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the given equation at given point x

    """
    return (x**5) - (5*(x**4)) + (8*(x**3) )- (5*(x**2)) + (11*x - 7)

def differentiatedFunction(x):
    """ Computes the value of the given equation (which is the differentiated
    form of the desired function f(x)) at point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the differentiated equation at given point x

    """
    return (5*(x**4)) - (20*(x**3))+ (24*(x**2)) - (10 *(x)) + 11

# Main Program

print '""""'
print 'NEWTONS METHOD FOR ROOT FINDING'
print '""""'
print ''

#User input
print("Enter the interval [a,b]")
start_point = int(input("Start point (a) = "))
end_point = int(input("End point (b) = "))
print("Enter your inital guess:")
initialP = int(input())
#Tolerance input
print("Please enter the tolerance in decimal form.")
tolerance = float(input())


print("So, the given error tolerance:", tolerance)
#calculation of first two points.. Iteration 1 and 2
point = initialP - (desiredFuncton(initialP) / differentiatedFunction(initialP))
point2 = point - (desiredFuncton(point) / differentiatedFunction(point))

#Choosing points for error check
pointAhead = point
pointLater = point2
#Error check by different 
difference = abs(pointLater - pointAhead)

iteration = 2 #Since we did two computation above, iteration starts from 2
while difference >= tolerance:
    iteration = iteration + 1
    point = pointLater - (desiredFuncton(pointLater) / differentiatedFunction(pointLater))
    pointAhead = pointLater
    pointLater = point
    difference = abs(pointLater - pointAhead)
    

print 'Root :' + str(pointLater)
pointLater = str(pointLater)
print 'Here's the point rounded off to 4 decimal place: ' + pointLater[0:6]
print 'Total number of Iteration to find the root' + str(iteration)
    
