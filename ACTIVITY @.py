num1 = int(input("Enter a number: ")) #globals
num2 = int(input("Enter another number: "))

def calculate_sum():
    sum = num1 + num2 #local
    print(sum)
def calculate_difference():
    difference = num1 - num2 #local
    print(difference)

calculate_sum()
calculate_difference()

