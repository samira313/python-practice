#Add numbers from 1 to 5
total = 0
for i in range(1, 6):
    total += i

print("Sum:", total)

#Nested loop to access inner list values
numbers = [[1, 2], [3, 4], [5, 6]]
for pair in numbers:
    for num in pair:
        print(num)


#Print numbers and their squares from 1 to 5
for i in range(1, 6):
    print(i, "squared is", i**2)

#Sum all numbers in a list
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print("Sum is:", total)

#Print each letter of the word "python
word = "python"
for letter in word:
    print(letter)

#Count how many times "o" appears
sentence = "I love python programming!"
count = 0
for char in sentence:
    if char == "o":
        count += 1
print("Number of 'o's:", count)

#Create a list of squares using loop
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)

#Print multiplication table of 5
for i in range(1, 11):
    print(f"5 * {i} = {5 * i}")
