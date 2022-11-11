# password generation methods 

def RandomPass():
    # import modules
    import random
    import string
    # get user input
    user_input = input("How many characters would you like your password to be? ")
    # add space between user input and next output
    print()
    # ask what % of password should be letters
    user_input2 = input("What percent of your password should be letters? ")
    # add space between user input and next output
    print()
    # ask what % of password should be numbers
    user_input3 = input("What percent of your password should be numbers? ")
    # add space between user input and next output
    print()
    # make remaining percent of password symbols
    user_input4 = 100 - int(user_input2) - int(user_input3)
    # print remaining percent of password symbols
    print("Your password will be " + str(user_input4) + "percent symbols.")
    print()

    # Check user input
    if user_input.isdigit() & user_input2.isdigit() & user_input3.isdigit():
        # generate password
        password = ''.join(random.choice(string.ascii_letters) for i in range(int(user_input) * int(user_input2) // 100))
        password += ''.join(random.choice(string.digits) for i in range(int(user_input) * int(user_input3) // 100))
        password += ''.join(random.choice(string.punctuation) for i in range(int(user_input) * int(user_input4) // 100))
        password = ''.join(random.sample(password, len(password)))
        # print password
        print("Your password is: " + password)
    else:
        # invalid input
        print("Invalid input. Please try again.")
        RandomPass()

def Diceware():
    # import modules
    import random
    # generate password
    password = random.randint(11111, 66666)
    # print password
    print(password)

def Passphrase():
    # ask for number of words
    num_words = input("How many words would you like your passphrase to be? ")
    # add space between user input and next output
    print()
    # Check user input
    if num_words.isdigit():
        # convert user input to int
        num_words = int(num_words)
        # get a wordlist from internet
        import urllib.request
        url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        # split wordlist into list
        wordlist = text.split()
        # import modules
        import random
        # generate password, add spaces between words
        password = ' '.join(random.sample(wordlist, num_words))
        # print password
        print(password)

def xkcd():
    # generate a password using xkcd method, 4-common words
    # import modules
    import random
    # get a wordlist from internet
    import urllib.request
    url = "https://raw.githubusercontent.com/bitcoin/bips/master/bip-0039/english.txt"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    # split wordlist into list
    wordlist = text.split()
    # print four random words with spaces between them
    print(random.choice(wordlist) + " " + random.choice(wordlist) + " " + random.choice(wordlist) + " " + random.choice(wordlist))


def RandomWalk():
    # generate a password using random walk method
    # tell user to smash keyboard and take input
    initialText = input("Please randomly smash your keyboard for 30 seconds, then click enter. ")
    # ask user how many characters they want
    user_input = input("How many characters would you like your password to be? ")
    # add space between user input and next output
    print()
    # Check user input
    if user_input.isdigit():
        # convert user input to int
        user_input = int(user_input)
        # trim input to specified length
        initialText = initialText[:user_input]
        # print password
        print(initialText)
        print()
        # disclaimer
        print("This password is not secure. It is only meant to be used for testing purposes.")
    else:
        # invalid input
        print("Invalid input. Please try again.")
        RandomWalk()
    
