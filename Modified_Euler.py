"""
This program utilizes modified Euler's method algorithm.
"""

def desiredFunction(t,y):
    """ Computes the value of the given equation at given point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the given equation at given point x

    """
    return float(((-t)*y)+(4*t*(y**(-1))))

#MAIN PROGRAM

print '""""'
print 'Modified Euler method'
print '""""'
print ''

#User Input
print("Please enter the interval a and b.")
start_point = float(input("Start point (a) ="))
end_point = float(input("End point (b) = "))
h = float(input("Please enter your step size (h)."))

initialValue = float(input("please enter the initial condition value at a."))

N = (end_point - start_point) / h

y = initialValue

for i in range(0, int(N)):
    t = start_point + h*i
    func1 = desiredFunction(t,y)
    func2 = desiredFunction(t+h, y + h*(func1))
    newY = y + (h/2)*(func1 + func2)
    y = newY

print 'Your desired value is' + stry(y)
    
