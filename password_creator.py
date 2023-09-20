print("Password creator with Caesar Cipher.")

key = input("What is the base of your password?: ")

password = ""

for character in key:
    if character.isalpha():
        if character.lower() == 'x':
            password += 'A'
        elif character.lower() == 'y':
            password += 'B'
        elif character.lower() == 'z':
            password += 'C'
        else:
            password += chr(ord(character) + 3)
    else:
        password += character

print(password)
