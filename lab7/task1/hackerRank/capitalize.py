def capitalize_name(name):
    
    words = name.split()
   
    capitalized_words = [word[0].upper() + word[1:] if word else '' for word in words]

    return ' '.join(capitalized_words)


full_name = input()
print(capitalize_name(full_name))