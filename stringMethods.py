mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())  
print(mixed_case.islower())  
print(mixed_case.upper())  
print(mixed_case.lower())  
print(mixed_case.istitle())  
title_case = mixed_case.title()
print(title_case)  
print(mixed_case.startswith("A"))  
print(mixed_case.endswith("e"))  
words = mixed_case.split()
print(words)  
print("".join(words).isalpha()) 


the_string = "North Dakota"
print(the_string.rjust(17))  
print(the_string.ljust(17, "*"))  
center_plus = the_string.center(16, "+")  
print(center_plus)
print(the_string.lstrip("North"))
print(center_plus.rstrip("+"))  
print(center_plus.strip("+"))  
print(the_string.replace("North", "South"))  

#String Reverser Solution
user_string = input("Please enter a string.")
reversed = ""
 
for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]
 
print(reversed)