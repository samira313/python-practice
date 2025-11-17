def count_chars(s):
   counts = {}

   for char in counts:
    if char in counts:
       counts[char] += 1
    else:
       counts[char] = 1   
    
print(count_chars("hello"))