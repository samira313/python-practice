# Read actual return date: day, month, year
actual_day, actual_month, actual_year = map(int, input().split())

# Read expected return date: day, month, year
expected_day, expected_month, expected_year = map(int, input().split())

# Initialize fine to 0
fine = 0

# Case 1: Book is returned in a later year
if actual_year > expected_year:
    fine = 60

# Case 2: Same year, but later month
elif actual_year == expected_year:
    if actual_month > expected_month:
        fine = (actual_month - expected_month) * 15
    # Case 3: Same month, but later day
    elif actual_month == expected_month and actual_day > expected_day:
        fine = (actual_day - expected_day) * 1

# Print the fine
print(fine)
