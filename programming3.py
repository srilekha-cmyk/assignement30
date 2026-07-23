def replace_vowels(s):
    r=""
    for i in s:
        if i in "aeiouAEIOU":
            r=r+"*"
        else:
            r=r+i
    return r

print(replace_vowels("Python Programming"))

# Output:
# Pyth*n Pr*gr*mm*ng
