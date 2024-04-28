import sys

def caesar_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            else:
                if shifted > ord('z'):
                    shifted -= 26
            result.append(chr(shifted))
        else:
            continue  # Skip non-alphabet characters

    # Group into blocks of five
    grouped = []
    for i in range(0, len(result), 5):
        grouped.append(''.join(result[i:i+5]))

    # Format output 10 blocks per line
    for i in range(0, len(grouped), 10):
        print(' '.join(grouped[i:i+10]))

if __name__ == "__main__":
    shift = int(sys.argv[1]) if len(sys.argv) > 1 else 3  # Default shift is 3
    for line in sys.stdin:
        caesar_cipher(line.strip().upper(), shift)
