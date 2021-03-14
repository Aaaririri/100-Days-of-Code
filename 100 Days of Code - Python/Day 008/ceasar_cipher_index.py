"""
same exercise as ceasr cipher but with a diferent aproach
"""
def encript(mensage, n):
    mensage_encription = mensage
    mensage_encription = list(mensage_encription)
    mensage_encripted = ''
    for i in range(0, len(mensage_encription)):
        if alphabet.index(mensage_encription[i]) + n < len(alphabet):
            mensage_encripted += alphabet[alphabet.index(mensage_encription[i]) + n]
        else:
            mensage_encripted += alphabet[alphabet.index(mensage_encription[i]) + n - len(mensage_encription)]
            
            
    return mensage_encripted

def decript(mensage, n):
    mensage_decryption = mensage
    mensage_decryption = list(mensage_decryption)
    mensage_decrypted = ''
    for i in range(0, len(mensage_decryption)):
        mensage_decrypted += alphabet[alphabet.index(mensage_decryption[i]) - n]

    return mensage_decrypted

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
state = True
while state:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text = encript(text, shift)
        print(text)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text = decript(text, shift)
        print(text)
    else:
        print('invalid arguments')
    state_aux = input("To continue making operation 'y' to stop 'n':")


    if state_aux == 'y':
        state = True
    elif state_aux == 'n':
        state = False
    else:
        state = False
