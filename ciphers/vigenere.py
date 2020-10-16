import string

class KeyNotProvided(Exception):
    pass

def encode(m:str ) -> str:
    mm = m.lower()
    mm = mm.replace(" ", "")
    return mm

class Alphabet:
    pass

class LatinAlphabet(Alphabet):

    def __init__(self):
        self.alph = string.ascii_lowercase

    def ord(self, char:str)->int:
        return self.alph.index(char)

    def char(self, index:int)->str:
        return self.alph[index]

    def len(self):
        return len(self.alph)

    def __len__(self):
        return self.len()

class Vigenere:

    def __init__(self, key:str, alphabet:Alphabet):

        if key == None or len(key) == 0:
            raise KeyNotProvided
        # TODO: Check that the alphabet is correct in the key
        self.key = key
        self.alphabet = alphabet

    def _cycle_key(self, key:str, message_len: int) -> str:
        """
        Crea una clave de igual longitud al mensaje repitiendo la
        misma.
        """
        return (key*(message_len//len(key) + 1))[:message_len]

    def encrypt(self, message:str)->str:
        """
        Dado un mensaje realizamos un cifrado de la forma
        C = (Mi + Ki) mod (len(alphabet))
        """

        mm = encode(message)
        key = self._cycle_key(self.key, len(mm))

        return ''.join(
            map(
                lambda (Mi,Ki):=x : self.alphabet.char((self.alphabet.ord(Mi) + self.alphabet.ord(Ki)) % self.alphabet.len()),
                zip(mm, key)
                )
            )

    def decrypt(self, message:str) -> str:
        """
        Dado un mensaje cifrado lo desciframos usando 
        C = (Mi - Ki) mod (len(alphabet))
        """

        mm = encode(message)
        key = self._cycle_message(self.key, len(mm))

        return ''.join(
            map(
                lambda (Mi, Ki) := x: self.alphabet.char((self.alphabet.ord(Mi) - self.alphabet.ord(Ki)) % self.alphabet.len()),
                zip(mm, key)
                )
            )

if __name__ == '__main__':

    V = Vigenere("tratra", LatinAlphabet())
    EC = V.encrypt("Have We not made the earth a resting place And the mountains as stakes And We created you in pairs")
    DC = V.decrypt(EC)

    print(f"Encrypted message: {EC}")
    print(f"Decrypted message: {DC}")
