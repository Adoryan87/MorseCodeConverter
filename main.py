from morse import ascii, MORSE_CODE_DICT


print(ascii)
print("Welcome to Morse Code converter!")


def to_morse():
    try:
        non_dictionary = ""
        storage = ""
        user_input = input("Enter a word or a sentence to convert into Morse Code: ").upper()
        for letter in user_input:
            if letter not in MORSE_CODE_DICT.keys():
                non_dictionary += letter
            storage += MORSE_CODE_DICT[letter.upper()] + " "
        print(f"Your encrypted message is {storage}")
    except KeyError:
        print(f"The following character '{non_dictionary}' is not in the Morse Code Dictionary.")



def to_text():
    reversed_dictionary = {v: k for k, v in MORSE_CODE_DICT.items()}
    user_input = input("Enter Morse Code to convert into word or sentence: ")
    storage = ""
    txt = user_input.split(' ')
    for letter in txt:
        storage += reversed_dictionary[letter]
    result = storage[:1].title() + storage[1:].lower()
    print(f"Your decrypted message is '{result}'.")


while True:
    choice = input(
        "Type 'Encrypt' to encrypt a message into Morse Code or 'Decrypt' to Transform it in to text, you can also "
        "say 'both': ").lower()
    if choice == "encrypt":
        to_morse()
        break
    elif choice == "decrypt":
        to_text()
        break
    elif choice == "both":
        to_morse()
        to_text()
        break
    else:
        print("Please Enter 'Encrypt' or 'Decrypt'")
