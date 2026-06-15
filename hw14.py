#Lambda Function: Write a lambda function that multiplies two numbers.

mul = lambda a,b: a*b
print(mul(2,3))

#Recursive Function: Write a recursive function that calculates the sum of the first n numbers.

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

#Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.

def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(10, 20, 30, 40))