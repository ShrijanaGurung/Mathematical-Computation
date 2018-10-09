"""
This program utilizes Composite Simpson's rule algorithm along with practical error bound
set up. I set up (n = 2) initially and value at n and n + 2 are computed
and are compared to get the difference
If the difference is within our tolerance, that's our answers for the given function.
"""
def function(x):
    """
    Computes the value of the given equation at given point x.
    The equation used for the computaton changes on the appromixation.
    Args:
        x: a single point between given intervals

    Returns:
        the value of the given equation at given point x

    """
    return 2/(1+x**3)

def computingH(start,end,num):
    """ Computes the h value i.e. the width of the subintervals.
    Args:
        start: The start point of given interval
        end: The end point of gvien interval
        total: Total number of sub intervals by which the given interval
        [start, end] is divided equally.

    Returns:
        The equal width of the each subintervals
    """

    return float((end - start)/num)

#MAIN PROGRAM

#User Input
print("Please enter your intervals, a and b.")
a = float(input("a = "))
b = float(input("b = "))
n = 2
errorTol = float(input("Enter your error tolerance."))
h = computingH(a,b,n)
####Value at the endpoints of the interval####
ValueAtA = function(a)
ValueAtB = function(b)


####First part
sumWithinOne = 0
point = (n/2)
for i in range(1,int(point)):
    number = 2* i
    xValue = a + (number * h)
    yValue = function(xValue)
  
    sumWithinOne = sumWithinOne + yValue

sumOne = 2 * sumWithinOne

#########secondPart
sumWithinTwo = 0
for i in range(1,int((n/2)+ 1)):
    number = (2*i) - 1
    xValue = a + (number * h)
    yValue = function(xValue)
    
    sumWithinTwo = sumWithinTwo + yValue

sumTwo = 4 * sumWithinTwo
total = ValueAtA + ValueAtB + sumOne + sumTwo

firstAns = (h/3) * total

n = n+ 2

##########Second value
h = computingH(a,b,n)
sumWithinOne = 0
point = (n/2)

for i in range(1,int(point)):
    number = 2* i
    xValue = a + (number * h)
    yValue = function(xValue)
    
    sumWithinOne = sumWithinOne + yValue

sumOne = 2 * sumWithinOne

#########secondPart
sumWithinTwo = 0
for i in range(1,int((n/2)+ 1)):
    number = (2*i) - 1
    xValue = a + (number * h)
    yValue = function(xValue)
    
    sumWithinTwo = sumWithinTwo + yValue

sumTwo = 4 * sumWithinTwo
total = ValueAtA + ValueAtB + sumOne + sumTwo

secondAns = (h/3) * total

while (abs(secondAns - firstAns)) >= errorTol:
    print("Error between the two values:",abs(secondAns - firstAns))
    print()
    print()
    n = n+2
    h = computingH(a,b,(n))
    sumWithinOne = 0
    point = (n/2)
    
    firstAns = secondAns
    for i in range(1,int(point)):
        number = 2* i
        xValue = a + (number * h)
        yValue = function(xValue)
       
        sumWithinOne = sumWithinOne + yValue
    sumOne = 2 * sumWithinOne

########secondPart
    sumWithinTwo = 0
    for i in range(1,int((n/2)+ 1)):
        number = (2*i) - 1
        xValue = a + (number * h)
        yValue = function(xValue)
        
        sumWithinTwo = sumWithinTwo + yValue

    sumTwo = 4 * sumWithinTwo
    total = ValueAtA + ValueAtB + sumOne + sumTwo
    Ans = (h/3) * total
    secondAns = Ans
    

print 'Error between the two values: ' + str(abs(secondAns - firstAns))
print 'When n : ' + str(n)
print 'The approximation is ' + str(secondAns)
    
    
