"""
This program utilzes Steffensen's method which is a similar root finding technique
as Netwon's method.
"""
def f(x):
    """ Computes the value of the given equation at given point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the given equation at given point x

    """
    return 2**(-x)

# MAin Program

#User input
print("Enter the interval [a,b]")
a = int(input("a = "))
b = int(input("b = "))
print("Your initial guess:")
initialP = int(input())
print("Please enter the tolerance in form of decimal.")
tolerance = float(input())
print("The tolerance:", tolerance)

#Evaluating the first pHAT value for further computation
p0 = initialP
p1 = f(p0)
p2 = f(p1)
firstDiff = p1 - p0
secondDiff = p2 - p1
difference = secondDiff - firstDiff
pHAT1 = (p0) - ( firstDiff**2)/difference

#Finding another pHAT, we'll use our first value of pHAT to compute
p0 = pHAT1
p1 = f(p0)
p2 = f(p1)
firstDiff = p1 - p0
secondDiff = p2 - p1
    
difference = secondDiff - firstDiff
pHAT2 = (p0) - ( firstDiff**2)/difference
error = abs(pHAT2 - pHAT1)

#Since two pHAT values are computes, we did two iteration
#for finding pHAT values
iteration = 2 
while error >= tolerance:
#Find new pHAT values
    pHAT1 = pHAT2
    p0 = pHAT2
    p1 = f(p0)
    p2 = f(p1)
    iteration = iteration + 1
    firstDiff = (p1 - p0)
    secondDiff = (p2 - p1)
    difference = (secondDiff - firstDiff)
    pHAT2 = ((p0) - (( firstDiff**2)/difference))

print 'The root : ' + str(pHAT2)
print 'The total number of iteration: ' + str(iteration)

    
