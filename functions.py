# Volume of a Rectangular Prism
length = 5
width = 8
height = 10

def calculate_rectangular(length, width, height):
    return length * width * height

print("Volume of rectangular prism:", calculate_rectangular(length, width, height))


# Celsius to Fahrenheit
def fahrenheit(celsius):
    return round((1.8 * celsius) + 32, 1)

c = int(input("Enter temperature in Celsius: "))
print(f"The Fahrenheit equivalent of {c} degrees Celsius is {fahrenheit(c)}")


# Return PI
def pi_returner():
    approx = 3.14
    return approx

print("Approximate value of Pi:", pi_returner())
