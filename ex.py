message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""

for char in message:
    if ord(char) >= 65 and ord(char) <= 90:
        new_char = (chr((((ord(char) - 65) + offset) % 26) + 65))
        encoded_message += new_char
    elif ord(char) >= 97 and ord(char) <= 122:
        new_char = (chr((((ord(char) - 97) + offset) % 26) + 97))
        encoded_message += new_char
    else:
        encoded_message += char

print (encoded_message)