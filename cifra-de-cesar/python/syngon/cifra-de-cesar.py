import os
import time
import re

TIMEWAITING = 2


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        # espaco
        if char == " ":
            result += " "

        #nao eh espaco
        else:
            # maiuscula
            if char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)

            # minuscula
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)

    return result


def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        # espaco
        if char == " ":
            result += ' '

        #nao eh espaco
        else:
            # maiuscula
            if char.isupper():
                result += chr((ord(char) + 26 - s - 65) % 26 + 65)

            # minuscula
            else:
                result += chr((ord(char) + 26 - s - 97) % 26 + 97)

    return result


def getShift():
    isCorrect = False

    while not isCorrect:
        shift = input("\nInsira o valor do shift ( entre 1 e 25 ): ")

        if shift.isnumeric() and (1 <= int(shift) <= 25):
            isCorrect = True
        else:
            print("\nInsira um numero entre 1 e 25 apenas!")
            time.sleep(TIMEWAITING)
            clear()
    return int(shift)


def has_number(text):
    return bool(re.search(r'\d', text))


def getText():
    isCorrect = False

    while not isCorrect:
        text = str(input("\nInsira o texto a ser encryptado: "))

        if not has_number(text):
            isCorrect = True
        else:
            print("\nInsira apenas letras!")
            time.sleep(TIMEWAITING)
            clear()
    return text


def getOp():
    isCorrect = False

    while not isCorrect:
        op = input("\nVoce deseja realizar uma nova operacao?\nDigite 1 para SIM e 0 para NAO\n")

        if op.isnumeric() and (int(op) == 1 or int(op) == 0):
            isCorrect = True
        else:
            print("\nInsira apenas 1 ou 0!")
            time.sleep(TIMEWAITING)
            clear()
    return int(op)

def resetValues(text, shift, textoEncryptado, textoDecryptado):
    text = ""
    textoEncryptado = ""
    textoDecryptado = ""
    shift = 0

    return text, shift, textoEncryptado, textoDecryptado

def main():
    x = True
    while x:
        clear()
        text = getText()
        shift = getShift()

        print("Texto input  : " + text)
        print("Valor modificador : " + str(shift))

        textoEncryptado = encrypt(text, shift)
        print("Texto encryptado: " + textoEncryptado)

        textoDecryptado = decrypt(textoEncryptado, shift)
        print("Texto decryptado: " + textoDecryptado)

        text, shift, textoEncryptado, textoDecryptado = resetValues(text, shift, textoEncryptado, textoDecryptado)
        x = getOp()


main()
