import math, pyperclip

plainttext = input("Enter your plain text: ")
key = int(input("Enter key: "))

ciphertext = [''] * key


for column in range(key):
    pointer = column;

    while pointer < len(plainttext):
        ciphertext[column] += plainttext[pointer]
        pointer+=key

print(''.join(ciphertext))

# Transposition Cipher Decryption

def main():
    myMessage = input("Enter cipher text: ")
    myKey = int(input("Enter key: "))

    text = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(text)

    pyperclip.copy(text)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / key))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    text = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        text[column] += symbol
        column += 1 # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(text)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()