def clean_string(s):
    return s.strip().lower()

def extract_substring(s,n):
    return s[n:]

def replace_vowels(s):
    r=""
    for i in s:
        if i in "aeiouAEIOU":
            r=r+"*"
        else:
            r=r+i
    return r

print(clean_string("   PYTHON Programming   "))
print(extract_substring("PythonProgramming",6))
print(replace_vowels("Python Programming"))
print("Python Java HTML".split())
print(",".join(["Python","Java","HTML"]))

# Output:
# python programming
# Programming
# Pyth*n Pr*gr*mm*ng
# ['Python', 'Java', 'HTML']
# Python,Java,HTML
