name="kanha"
print(len(name))
L=len(name)
print(L)
print(name.endswith("nha"))
print(name.startswith("ka"))
print(name.capitalize()) # Capitalize only first letter

text = "  Hello Python  "

print(text.lower())          # hello python
print(text.upper())          # HELLO PYTHON
print(text.strip())          # Hello Python
print(text.replace("Python", "World"))  # Hello World
print(text.split())          # ['Hello', 'Python']
print(text.startswith(" "))  # True
print(text.endswith(" "))    # True
print(text.find("Python"))   # 8
print(text.count("o"))       # 2