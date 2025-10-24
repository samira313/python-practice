# Define a dictionary to store student names and their list of grades
gradebook = {}

# Define a function to calculate average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Start infinite loop to show the menu until user exits
while True:
    print("\n--- Student Gradebook ---")
    print("1. Add student and grades")
    print("2. Show all students and averages")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    # Option 1: Add a new student
    if choice == "1":
        name = input("Enter student name: ").capitalize()
        grades_input = input("Enter grades separated by commas (e.g. 18,20,17): ")
        grades_list = [float(g.strip()) for g in grades_input.split(",")]
        gradebook[name] = grades_list
        print(f"Student {name} added successfully.")

    # Option 2: Show all students with their average grade
    elif choice == "2":
        if not gradebook:
            print("No students added yet.")
        else:
            for student, grades in gradebook.items():
                average = calculate_average(grades)
                print(f"{student}: Grades = {grades} | Average = {average:.2f}")

    # Option 3: Exit the program
    elif choice == "3":
        print("Goodbye!")
        break

    # Invalid input
    else:
        print("Invalid choice. Please select 1, 2 or 3.")
