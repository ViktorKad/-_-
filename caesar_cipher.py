# -*- coding: UTF-8 -*-
# Python 2.7

shift = input("Enter the shift (number)\n")
sourceStr = raw_input("\nEnter the message\n")

alphabet = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
alphabetLen = len(alphabet)

while shift > alphabetLen:
    shift = alphabetLen - shift

def getCaesarCipher(sourceStr, shift):
    cipher = []
    for nextChar in sourceStr:
        if alphabet.find(nextChar) != -1 or nextChar == " ":
            positionNum = alphabet.find(nextChar) + shift
            positionNum = positionNum if positionNum < alphabetLen else positionNum - alphabetLen
            nextChar = nextChar if nextChar == " " else alphabet[positionNum]
            cipher.append(nextChar)

    return cipher

caesarCipher = getCaesarCipher(sourceStr, shift)

print '\nCaesar cipher', ''.join(caesarCipher)

raw_input("\nPress Enter")