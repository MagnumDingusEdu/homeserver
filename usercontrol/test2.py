
a = input()
b = ''
for character in a:
    if character == 'A':
        character = str(0)
    if character == 'B':
        character = str(1)
    b += character
print(b)