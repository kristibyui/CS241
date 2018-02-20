"""
CS241 Homework 7
Written by Chad Macbeth
"""

def fib(n):
   # Base Cases
   if n <= 0:
      return 0
   elif n == 1:
      return 1
   elif n == 2:
      return 1

   # By definition: fib(n) = fib(n-1) + fib(n-2)
   return fib(n-1) + fib(n-2)

# Print out the first 20 fib numbers
for i in range(20):
   print("fib({}) = {}" .format(i, fib(i)))

