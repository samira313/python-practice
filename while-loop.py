#Print numbers 1 to 5 using while loop
i = 1
while i <= 5:
    print(i)
    i += 1

#Countdown from 3 to 1, then print "Liftoff
count = 3
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

#Ask user to enter correct password until it's correct
password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access granted.")

#Infinite loop until user types "exit
while True:
    word = input("Type 'exit' to stop: ")
    if word == "exit":
        break
    
#Print only even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
