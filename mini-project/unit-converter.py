#  Define function to convert kilometers to miles
def km_to_miles(km):
    return km * 0.621371

#  Define function to convert Celsius to Fahrenheit
def c_to_f(celsius):
    return (celsius * 9/5) + 32

#  Define function to convert centimeters to inches
def cm_to_inch(cm):
    return cm / 2.54

#  Start an infinite loop to keep showing the menu until user chooses to exit
while True:
    # 📋 Display the menu options
    print("\n Unit Converter Menu:")
    print("1. Kilometer → Miles")
    print("2. Celsius → Fahrenheit")
    print("3. Centimeter → Inch")
    print("4. Exit")

    #  Get the user's choice
    choice = input("Choose an option (1-4): ")

    #  Option 1: KM → Miles
    if choice == "1":
        km = float(input("Enter kilometers: "))  # Get input in kilometers
        result = km_to_miles(km)                # Convert to miles
        print(f"{km} km = {result:.2f} miles")  # Print result with 2 decimals

    #  Option 2: Celsius → Fahrenheit
    elif choice == "2":
        celsius = float(input("Enter Celsius: "))  # Get input in Celsius
        result = c_to_f(celsius)                   # Convert to Fahrenheit
        print(f"{celsius}°C = {result:.2f}°F")     # Show result

    # Option 3: CM → Inches
    elif choice == "3":
        cm = float(input("Enter centimeters: "))   # Get input in cm
        result = cm_to_inch(cm)                    # Convert to inches
        print(f"{cm} cm = {result:.2f} inches")    # Display result

    #  Option 4: Exit program
    elif choice == "4":
        print("Goodbye")  # Exit message
        break                # Stop the loop and end program

    #  Invalid input handler
    else:
        print("Invalid choice. Please select between 1 and 4.")
