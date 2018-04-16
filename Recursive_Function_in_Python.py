# File: Recursive_Function_in_Python.py
# Description: Using recursive function to calculate Fibonacci value
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Using recursive function to calculate Fibonacci value // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Recursive_Function_in_Python (date of access: XX.XX.XXXX)

# Implementing task to calculate Fibonacci value
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

y = fib(5)
print(y)
