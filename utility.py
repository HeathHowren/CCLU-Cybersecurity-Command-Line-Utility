# python command line utility for cybersecurity

# Imports
import os
import encryption


# Global variables

# Functions

# Menu
def menu():
    # Print the menu to the command line
    print()
    print("Menu:")
    print("1. Encryption")
    print("2. Decryption")
    print("4. Password")
    print("5. Network")
    print("Q. Exit")
    print()

# Main
def main():
    # Print the title to the command line
    print("*" * 50)
    print("CCLU - Cybersecurity Command Line Utility")
    print("It\'s pronounces \"See Clue\".")
    print("*" * 50)
    menu()
    print()
    user_input = input("Please select an option: ")
    # Check user input
    if user_input == "1" or user_input == "Encryption":
        # clear the screen
        os.system("cls")
        # Encryption
        print("Encryption methods: ")
        print("1. Caesar")
        print("2. Vigenere")
        print("3. RSA")
        print("4. AES")
        print("5. DES")
        print("6. Blowfish")
        print("7. RC4")
        print("8. MD5")
        print("9. SHA-1")
        print("10. SHA-256")
        print("11. SHA-512")
        print("12. SHA-3")
        print("13. HMAC")
        print("14. PBKDF2")
        print("15. Scrypt")
        print("16. Bcrypt")
        print("17. Argon2")
        print("18. Elliptic Curve")
        print("19. Diffie-Hellman")
        print()
        # get user input
        user_input = input("Please select an option: ")
        # add space between user input and next output
        print()
        # Check user input
        if user_input == "1" or user_input == "Caesar":
            # Caesar
            print("Caesar Cipher (Shift)")
            from encryption import Caesar
            Caesar()
        if user_input == "2" or user_input == "Vigenere":
            # Vigenere
            print("Vigenere")
            from encryption import Vigenere
            Vigenere()
        if user_input == "3":
            # RSA
            print("RSA")
            from encryption import RSA
            RSA()
        if user_input == "4":
            # AES
            print("AES")
            from encryption import AES
            AES()
        if user_input == "5":
            # DES
            print("DES")
            from encryption import DES
            DES()
        if user_input == "6":
            # Blowfish
            print("Blowfish")
            from encryption import Blowfish
            Blowfish()
        if user_input == "7":
            # RC4
            print("RC4")
            from encryption import RC4
            RC4()
        if user_input == "8":
            # MD5
            print("MD5")
            from encryption import MD5
            MD5()
        if user_input == "9":
            # SHA-1
            print("SHA-1")
            from encryption import SHA1
            SHA1()
        if user_input == "10":
            # SHA-256
            print("SHA-256")
            from encryption import SHA256
            SHA256()
        if user_input == "11":
            # SHA-512
            print("SHA-512")
            from encryption import SHA512
            SHA512()
        if user_input == "12":
            # SHA-3
            print("SHA-3")
            from encryption import SHA3
            SHA3()
        if user_input == "13":
            # HMAC
            print("HMAC")
            from encryption import HMAC
            HMAC()
        if user_input == "14":
            # PBKDF2
            print("PBKDF2")
            from encryption import PBKDF2
            PBKDF2()
        if user_input == "15":
            # Scrypt
            print("Scrypt")
            from encryption import Scrypt
            Scrypt()
        if user_input == "16":
            # Bcrypt
            print("Bcrypt")
            from encryption import Bcrypt
            Bcrypt()
        if user_input == "17":
            # Argon2
            print("Argon2")
            from encryption import Argon2
            Argon2()
        if user_input == "18":
            # Elliptic Curve
            print("Elliptic Curve")
            from encryption import EllipticCurve
            EllipticCurve()
        if user_input == "19":
            # Diffie-Hellman
            print("Diffie-Hellman")
            from encryption import DiffieHellman
            DiffieHellman()

    elif user_input == "2" or user_input == "Decryption":
        # Decryption
        print("Decryption")
    elif user_input == "3" or user_input == "Password":
        # Password Generator
        print("Password")
    elif user_input == "Q" or user_input == "q":
        # Exit
        print("Exiting...")
    else:
        # Invalid input
        print("Invalid input. Please try again.")
        main()

# Run the main function
if __name__ == "__main__":
    main()
