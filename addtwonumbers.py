
a=12
b=3
c = a+b
print("sum of ",a, "and ",b ,"is", c)

#----------------------"add input with user inputs"

input1 = input("enter first number: ")
input2 = input("enter second number: ")
sum2 = float(input1)+float(input2)
print ("The sum of {0} and {1} is {2}" . format(input1,input2,sum2))

#--------------------------Add Two Numbers in Python Using Function

def sum(a,b):
    return a+b
n1=3
n2=6
sum_of_two = sum(n1,n2)
print ("The sum of {0} and {1} is {2}" . format(n1,n2,sum_of_two))

#-----------------------Add Two Numbers Using operator.add() Method

NUM1=1
NUM2=3

import operator
NUM = operator.add(NUM1,NUM2)
print ("The sum of {0} and {1} is {2}" . format(NUM1,NUM2,NUM))

#------------Add Two Number Using Lambda Function


add_numbers = lambda x, y: x + y

num1 = 1
num2 = 2

result = add_numbers(num1, num2)

print("The sum of", num1, "and", num2, "is", result)