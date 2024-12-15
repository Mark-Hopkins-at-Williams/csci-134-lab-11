def associate(keys, values):
    """ Replace this with your code for Question One ("Cipher"). """


class Cipher:
    """ Do not modify this class! """
    def __init__(self, alphabet, codes):
        self.deciphered = associate(codes, alphabet)
        self.enciphered = associate(alphabet, codes)

    def decipher(self, code):
        if code in self.deciphered:
            return self.deciphered[code]
        else:
            return "*"

    def encipher(self, letter):
        if letter in self.enciphered:
            return self.enciphered[letter]
        else:
            return "*"

    def viz(self, code):
        return str(code)

    def print(self, code):
        print(self.viz(code))


def shift_alphabet(shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return alphabet[shift:] + alphabet[:shift]


class CaesarCipher(Cipher):
    """ An example cipher. """
    def __init__(self, shift):
        super().__init__(shift_alphabet(0), shift_alphabet(shift))
