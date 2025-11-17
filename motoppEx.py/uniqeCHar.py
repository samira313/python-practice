def uniqe_char(str):
    unique = str.replace(' ', '')
    
    return sorted(set(unique))
print(uniqe_char("hello world"))