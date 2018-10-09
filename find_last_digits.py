"""
The program gives us the desired last few digits of
7 raised to the power of 2015 (7^2015).
This program can be modified to get results for different larger computation.
Note: This is to avoid complex large computation and to get desired value for
other theory or proofs.
"""
print("Enter stop to end the program.")
print("Please enter the number of digit you want to find.")
desiredDigits = int(input())

while desiredDigits != "stop":
    number = 4
    if desiredDigits > 1:
        for i in range(desiredDigits):
            number = number * 10
    digit = 1
    remainder = 2015 % number
    for i in range(remainder):
        digit = str(digit * 7)
         
        reverseDigit = digit[::-1]
          
        newDigit = reverseDigit[0: desiredDigits]
        digit = int(newDigit[::-1])

    if len(str(digit)) != desiredDigits:
        digit = '0' + str(digit)

    print 'The last ' + str(desiredDigits) + 'digits:' + str(digit)
    print("Please enter the number of digit you want to find.")
    desiredDigits = int(input())
