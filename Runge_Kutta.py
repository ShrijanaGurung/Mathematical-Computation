"""
The program utilizes Runge Kutta Method algorithm which is an iterative
method to approximate solutons to differential equations.
"""
def function(t,y):
    return float(((-t)*y)+(4*t*(y**(-1))))

#MAIN PROGRAM
print '""""'
print 'Runge Kutta method.'
print '""""'
print ''

#User Input
print("Please enter the interval a and b.")
start_point = float(input("Start point (a) ="))
end_point = float(input("End point (b) = "))
h = float(input("Please enter your step size (h)."))
initialValue = float(input("please enter the initial condition value at a."))

N = (b - a) / h

y = initialValue
for i in range(0, int(N)):
    t = a + h*i
    func1 = h*function(t,y)
    func2 = h*function(t+(h/2), y + (1/2)*(func1))
    func3 = h*(function(t+(h/2), y + (1/2)*func2))
    func4 = h*(function(t + h, y + func3))
    newY = y + ((1/6)*(func1 + (2*func2)+(2*func3) + func4))
    y = newY

print 'The desired value is : ' + str(y)
