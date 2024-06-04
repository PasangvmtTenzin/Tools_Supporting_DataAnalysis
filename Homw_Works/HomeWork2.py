MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}#full virsion code from wekipedia

print("Morse Code For Referance\n",MORSE_CODE_DICT)

# encode a message to Morse code
def encode_morse(message):
    encoded_message = []
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            encoded_message.append(MORSE_CODE_DICT[char])
        elif char.isalnum():
            encoded_message.append(char)  # Ignoring non-alphanumeric characters
    return '/'.join(encoded_message)

# decode Morse code to a message
def decode_morse(morse_code):
    decoded_message = []
    for code in morse_code.split('/'):
        for letter, morse in MORSE_CODE_DICT.items():
            if morse == code:
                decoded_message.append(letter)
                break
        else:
            decoded_message.append(code)  # Keeping unknown Morse code intact
    return ''.join(decoded_message)

# Main function to handle user input and call functions
def main():
    choice = input("Enter 'encode' to encode a message or 'decode' to decode a message: ").lower()
    if choice == 'encode':
        message = input("Enter the message to encode: ")
        encoded_message = encode_morse(message)
        print("Encoded message:", encoded_message)
    elif choice == 'decode':
        morse_code = input("Enter the Morse code to decode: ")
        decoded_message = decode_morse(morse_code)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")

if __name__ == "__main__":
    main()


#Zażółć gęślą jaźń