import itertools as it
import math as m

class Vigenere:
    
    def __init__(self, key):
        self._key = key.upper().strip().replace(' ', '')
        letters = list(map(chr, range(65, 91)))
        self._tabula_recta = {}
        self._reverse_tabula_recta = {}
        for idx, letter in enumerate(letters):
            contents = letters.copy()
            contents = [
                contents[(idj + idx) % len(contents)] 
                for idj, _ 
                in enumerate(letters)
            ]
            self._tabula_recta[letter] = dict(it.zip_longest(letters, contents))
            self._reverse_tabula_recta[letter] = {v: k for k, v in self._tabula_recta[letter].items()}
            
    def encipher(self, plaintext):
        plaintext = plaintext.upper().strip().replace(' ', '')
        coordinates = [
            (self._key[idx % len(self._key)], plaintext_letter) 
            for idx, plaintext_letter 
            in enumerate(plaintext)
        ]
        
        ciphertext = ''
        for coordinate in coordinates:
            ciphertext += self._tabula_recta[coordinate[0]][coordinate[1]]
            
        return ciphertext
    
    def decipher(self, ciphertext):
        ciphertext = ciphertext.upper().strip().replace(' ', '')
        coordinates = [
            (self._key[idx % len(self._key)], ciphertext_letter) 
            for idx, ciphertext_letter 
            in enumerate(ciphertext)
        ]
        
        plaintext = ''
        for coordinate in coordinates:
            plaintext += self._reverse_tabula_recta[coordinate[0]][coordinate[1]]
                    
        return plaintext

#Bifid Cipher

def pair(it):
    it = iter(it)
    while True:
        try:
            yield next(it), next(it)
        except StopIteration:
            return

class Bifid:
    
    def __init__(self):
        self.ks_1 = {
            '1': {'1': 'P', '2': 'H', '3': 'Q', '4': 'G', '5': 'M'},
            '2': {'1': 'E', '2': 'A', '3': 'Y', '4': 'L', '5': 'N'},
            '3': {'1': 'O', '2': 'F', '3': 'D', '4': 'X', '5': 'K'},
            '4': {'1': 'R', '2': 'C', '3': 'V', '4': 'S', '5': 'Z'},
            '5': {'1': 'W', '2': 'B', '3': 'U', '4': 'T', '5': 'I'}
        }
        self.ks_2 = {
            'A': (2, 2), 'B': (5, 2), 'C': (4, 2), 'D': (3, 3), 'E': (2, 1),
            'F': (3, 2), 'G': (1, 4), 'H': (1, 2), 'I': (5, 5), 'K': (3, 5),
            'L': (2, 4), 'M': (1, 5), 'N': (2, 5), 'O': (3, 1), 'P': (1, 1),
            'Q': (1, 3), 'R': (4, 1), 'S': (4, 4), 'T': (5, 4), 'U': (5, 3), 
            'V': (4, 3), 'W': (5, 1), 'X': (3, 4), 'Y': (2, 3), 'Z': (4, 5), 'J': (5, 5)
        }
        return

    def encipher(self, plaintext):
        plaintext = plaintext.upper().strip().replace(' ', '')
        l1 = [self.ks_2[c] for c in plaintext]
    
        ls = []
        for i in range(1, m.floor(len(l1) / 5) + 2):
            ls.append(l1[(i-1)*5:i*5])
            
        ret = ''
        for fiver in ls:
            l2 = [l[0] for l in fiver]
            l3 = [l[1] for l in fiver]
            l2 += l3
            cipherlist = [self.ks_1[str(p[0])][str(p[1])] for p in pair(l2)]
            ret += ''.join(cipherlist)
            
        return ret
    
    def decipher(self, ciphertext):
        l1 = [self.ks_2[c] for c in ciphertext]
        l1 = [item for sublist in l1 for item in sublist]
        
        ls = []
        for i in range(1, m.floor(len(l1) / 10) + 2):
            ls.append(l1[(i-1)*10:i*10])
            
        ret = ''
        for tenner in ls:
            l2 = []
            for i in range(0,int(len(tenner)/2)):
                l2.append((tenner[i], tenner[i + int(len(tenner)/2)]))
            
            plaintextlist = [self.ks_1[str(p[0])][str(p[1])] for p in l2]
            ret += ''.join(plaintextlist)
                
        return ret
    
bifid = Bifid()

def apply_cipher(cipher, plaintext, key, iv=''):
    plaintext = plaintext.upper().strip().replace(' ', '')
     
    slices = [plaintext[i:i+5] for i in range(0, len(plaintext), 5)]
    slices = [slice if len(slice) == 5 else slice + 'X' * (5 - len(slice)) for slice in slices]
    
    enciphered_slices = []
    for i, slice in enumerate(slices):
        # Convert the counter to a letter, starting from A
        cntr = chr(i + 65)
        
        # Prepend the IV to the counter, pad the counter so the 
        # combined string is the same length as a block
        iv_cntr = iv.upper() + 'X' * (5 - (len(cntr) + len(iv))) + cntr
        
        # Encipher the IV|CNTR string
        cipher_cntr = cipher.encipher(iv_cntr)
        
        ciphered_slice = Vigenere(cipher_cntr).encipher(slice)
        enciphered_slices.append(ciphered_slice)
    
    
    enciphered_slices = [cipher.encipher(iv + slice) for slice in slices]
    print('<=== ({})'.format(type(cipher)))
    print('Blocked ciphertext\t {}'.format(''.join(enciphered_slices)))
    print('Non-blocked ciphertext\t {}'.format(cipher.encipher(plaintext)))
    print('===>')

plaintext = 'Are you the keymaster'
key = 'OnlyZuul'
vigenere = Vigenere(key.upper())

iv = 'ab'
apply_cipher(cipher=vigenere, plaintext=plaintext, key=key, iv=iv)
apply_cipher(cipher=bifid, plaintext=plaintext, key=key, iv=iv)

iv = 'cd'
apply_cipher(cipher=vigenere, plaintext=plaintext, key='', iv=iv)
apply_cipher(cipher=bifid, plaintext=plaintext, key='', iv=iv)