# encryption methods

def Caesar():
    user_input = input("Please enter a message: ")
    # add space between user input and next output
    print()
    # ask for Shift/Key(number)
    shiftKey = input("Please enter a Shift/Key (number: pos = right shift, neg = left shift): ")
    # sanitize user input
    shiftKey = int(shiftKey)
    # add space between user input and next output
    print()
    print("1. Use the English alphabet (26 letters from A to Z)")
    print("2. Use the English alphabet and also shift the digits 0-9")
    print("3. Use the latin alphabet in the time of Caesar (23 letters, no J, U or W)")
    print("4. Use the ASCII Table (0-127) as Alphabet")
    print("5. Use a custom alphabet (A-Z chars, 0-9 digits only)")
    option_input = input("Please select an option: ")

    if option_input == "1":
        # English alphabet (26 letters from A to Z)
        print("English alphabet (26 letters from A to Z)")
        # define the array to be used for shift
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # shift user_input by shiftKey
        cipher = ""
        # account for lowercase letters
        user_input = user_input.upper()
        for char in user_input:
            if char in alphabet:
                position = alphabet.find(char)
                newPosition = (position + shiftKey) % 26
                newChar = alphabet[newPosition]
                cipher += newChar
            else:
                cipher += char
        print("Encrypted message: " + cipher)
        
    elif option_input == "2":
        # English alphabet and also shift the digits 0-9
        print("English alphabet and also shift the digits 0-9")
        # define the array to be used for shift
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        # shift user_input by shiftKey
        cipher = ""
        # account for lowercase letters
        user_input = user_input.upper()
        for char in user_input:
            if char in alphabet:
                position = alphabet.find(char)
                newPosition = (position + shiftKey) % 36
                newChar = alphabet[newPosition]
                cipher += newChar
            else:
                cipher += char
        print("Encrypted message: " + cipher)

    elif option_input == "3":
        # latin alphabet in the time of Caesar (23 letters, no J, U or W)
        print("latin alphabet in the time of Caesar (23 letters, no J, U or W)")
        # define the array to be used for shift (alphabet but no J, U or W)
        alphabet = "ABCDEFGHIKLMNOPQRSTVXYZ"
        # shift user_input by shiftKey
        cipher = ""
        # account for lowercase letters
        user_input = user_input.upper()
        for char in user_input:
            if char in alphabet:
                position = alphabet.find(char)
                newPosition = (position + shiftKey) % 23
                newChar = alphabet[newPosition]
                cipher += newChar
            else:
                cipher += char
        print("Encrypted message: " + cipher)

    elif option_input == "4":
        # ASCII Table (0-127) as Alphabet
        print("ASCII Table (0-127) as Alphabet")
        # define the array to be used for shift ASCII Table (0-127)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        # shift user_input by shiftKey
        cipher = ""
        for char in user_input:
            if char in alphabet:
                position = alphabet.find(char)
                newPosition = (position + shiftKey) % 128
                newChar = alphabet[newPosition]
                cipher += newChar
            else:
                cipher += char
        print("Encrypted message: " + cipher)

    elif option_input == "5":
        # custom alphabet (A-Z chars, 0-9 digits only)
        print("Custom alphabet")
        # ask user to input alphabet
        alphabet = input("Please enter a custom alphabet (A-Z chars, 0-9 digits only): ")
        # shift user_input by shiftKey
        cipher = ""
        for char in user_input:
            if char in alphabet:
                position = alphabet.find(char)
                newPosition = (position + shiftKey) % len(alphabet)
                newChar = alphabet[newPosition]
                cipher += newChar
            else:
                cipher += char
        print("Encrypted message: " + cipher)

    else:
        # invalid input
        print("Invalid input. Please try again.")

def Vigenere():
    # encryption using Vigenere Cipher
    user_input = input("Please enter a message: ")
    # add space between user input and next output
    print()
    # ask for a Cipher Key (string)
    cipherKey = input("Please enter a Cipher Key (string): ")
    # add space between user input and next output
    print()
    # ask use if they want a custom alphabet or default alphabet
    print("1. Use the English alphabet (26 letters from A to Z)")
    print("2. Use a custom alphabet")
    option_input = input("Please enter a number: ")
    # add space between user input and next output
    print()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if option_input == "1":
        # do nothing
        print("Using the English alphabet (26 letters from A to Z)")
    elif option_input == "2":
        # ask user to input alphabet
        alphabet = input("Please enter a custom alphabet (example format: ABCDEFabcdef): ")
    else:
        # invalid input
        print("Invalid input. Please try again.")
    # add space between user input and next output
    print()
    # encrypt message
    cipher = ""
    # account for lowercase letters in user input
    user_input = user_input.upper()
    # account for lowercase letters in cipher key
    cipherKey = cipherKey.upper()
    # loop through user input
    for i in range(len(user_input)):
        # account user input not in alphabet
        if user_input[i] not in alphabet:
            cipher += user_input[i]
        else:
            # get position of current char in alphabet
            position = alphabet.find(user_input[i])
            # get position of current char in cipher key, account for if cipher key is shorter than user input
            if i >= len(cipherKey):
                keyPosition = alphabet.find(cipherKey[i % len(cipherKey)])
            else:
                keyPosition = alphabet.find(cipherKey[i])
            # get new position by adding position and keyPosition
            newPosition = (position + keyPosition) % len(alphabet)
            # get new char by using new position
            newChar = alphabet[newPosition]
            # add new char to cipher
            cipher += newChar
    print("Encrypted message: " + cipher)

'''
def RSA():

def AES():

def DES():

def Blowfish():

def RC4():

def MD5():

def SHA1():

def SHA256():

def SHA512():

def SHA3():

def HMAC():

def PBKDF2():

def Scrypt():

def Bcrypt():

def Argon2():

def EllipticCurve():

def DiffieHellman():
'''