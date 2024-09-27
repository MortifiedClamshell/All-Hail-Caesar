secret_message = "There is no way a bee should be able to fly. It's wings are too small to get its fat little body off the ground. 4487"
number = 3

def word_changer(text: str, shift: int):
    result = ""

    for char in text:
        if char.islower():
            result  += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isupper():
            result  += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isdigit():
            result  += chr((ord(char) + shift - 48) % 10 + 48)
        else:
            result += char

    return result

def word_fixer(text: str, shift: int):
    result = ""

    for char in text:
        if char.islower():
            result  += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.isdigit():
            result  += chr((ord(char) - shift - 48) % 10 + 48)
        else:
            result += char

    return result

hidden_message = word_changer(secret_message, number)
print(word_changer(secret_message, number))

print(word_fixer(hidden_message, number))





