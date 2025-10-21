numbers = [15, 30, 40, 60, 70, 85]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} is FizzBuzz")
    elif num % 3 == 0:
        print(f"{num} is Fizz")
    elif num % 5 == 0:
        print(f"{num} is Buzz")
    else:
        print(f"{num} is not FizzBuzz")
