
sideA=float(input("Enter the side A: "))
sideB=float(input("Enter the side B: "))
#The input for both variables

import math
squaredA = math.pow(sideA,2)
squaredB = math.pow(sideB,2)
#gets the square of both numbers
sumofboth = squaredA + squaredB
hp=math.sqrt(sumofboth)
#Gets the hypotenuse

print(f"the hypotenuse is: {hp:.2f}")
21