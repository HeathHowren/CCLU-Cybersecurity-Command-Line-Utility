# imports
import os

# dependent function... *vomits everywhere because math*
def egcd(a, b):
    # extended Euclidean algorithm
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    # modular multiplicative inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def gcd(a, b):
    # greatest common divisor
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # least common multiple
    return a * b // gcd(a, b)

def isPrime(n):
    # check if number is prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


# encryption methods
def Caesar():
    # clear screen
    os.system('cls')
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
    # clear screen
    os.system('cls')
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
 

def RSA():
    # clear screen
    os.system('cls')
    # I have already completed Calculus 1 & 2, why am I torturing myself with this?
    print("NOTE: If you're like a multi-million dollar corporation... double check my math before implementing this... not my fault")
    print()
    print("What would you like to do?")
    print("1. Generate a key pair")
    print("2. Encrypt a message using a key pair")
    option_input = input("Please enter a number: ")
    if option_input == "1":
        GenerateKeysRSA()
    elif option_input == "2":
        # ask user for user input, n, e
        user_input = input("Please enter a message: ")
        n = int(input("Please enter n: "))
        e = int(input("Please enter e: "))
        EncryptRSA(user_input, n, e)
    else:
        # invalid input
        print("Invalid input. Please try again.")
        option_input = input("Please enter a number: ")


def GenerateKeysRSA():
# generaring key pair
    user_input = input("Please enter the plaintext to encrypt: ")
    # add space between user input and next output
    print()
    # ask user to input a prime number
    p = int(input("Please enter a prime number (p) [the bigger the better]: "))
    # check if p is prime
    if isPrime(p) == False:
        print("p is not prime. Please try again.")
        print()
        p = int(input("Please enter a prime number (p) [the bigger the better]: "))
    # add space between user input and next output
    print()
    # ask user to input a prime number
    q = int(input("Please enter a prime number (q) [the bigger the better]: "))
    # check if q is prime
    if isPrime(q) == False:
        print("q is not prime. Please try again.")
        print()
        q = int(input("Please enter a prime number (q)[the bigger the better]: "))
    # add space between user input and next output
    print()
    # calculate n
    n = p * q
    # print n
    print("n = p * q = " + str(n))
    print()
    # calculate tot(n), Carmichael's totient function; what Car does Michael drive?
    tot_n = lcm(p - 1, q - 1)
    print("tot(n) = λ(n) = lcm(p - 1, q - 1) = " + str(tot_n))
    print()
    # not using euler's totient function because it's not as efficient plus I'm a savage mfer
    # give examples of e
    print("Examples of e: 3, 5, 17, 257, 65537, etc.")
    # ask for user input e, where 1 < e <tot(n) and e is coprime to tot(n)
    e = int(input("Please enter a number (e) where 1 < e < tot(n) and e is coprime to tot(n): "))
    # test that e is coprime to tot(n) and 1 < e < tot(n)
    if gcd(e, tot_n) != 1 or e < 1 or e > tot_n:
        print("Invalid input. Do you seriously not know how to check that gcd(e, tot_n) != 1 or e < 1 or e > tot_n; kinda embarrassing. lease try again.")
    # define phi
    phi = (p - 1) * (q - 1) # omg its euler's totient making a comeback, remeber earlier when I said I'm a savage mfer? well I lied
    # calculate d
    d = modinv(e, phi)
    # print d
    print("d = modinv(e, phi) = " + str(d))
    print()
    # print public key
    print("Public key (n, e): (" + str(n) + ", " + str(e) + ")")
    # print private key
    print("Private key (n, d): (" + str(n) + ", " + str(d) + ")")
    print()
    # ask user if they want to encrypt a message using the key
    print("Would you like to encrypt a message using the key we just made?")
    print("1. Yes")
    print("2. No")
    option_input = input("Please enter a number: ")
    if option_input == "1":
        EncryptRSA(user_input, n, e)


def EncryptRSA(user_input, n, e):
    # encrypt message
    cipher = ""
    for char in user_input:
        # convert char to ascii
        char = ord(char)
        # encrypt char
        char = pow(char, e, n)
        # convert char back to ascii
        char = chr(char)
        # add char to cipher
        cipher += char
    print("Encrypted message: " + cipher)
    
'''
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
