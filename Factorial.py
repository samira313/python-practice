def factorial(n):
   result = 1
   for i in range(1,  n + 1):
      result *= i
   return result

print(factorial(3))
print(factorial(4))
print(factorial(5))