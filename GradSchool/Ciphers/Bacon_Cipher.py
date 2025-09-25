"""

Assignment: A New Substitute
Alex Hostick
ECE595, Spring 2H
Section 3N9

Tutorial (for when I look back at this assignment):
https://www.youtube.com/watch?v=SXOoICf2DgU

This cipher may be easier to crack than caesar ciphers as
it has a recognizable pattern. Adding a second cipher, such as
a caesar cipher on the bacon cipher plaintext, or extra letters
for a higher dimension of possibilities, may make it more
robust.

"""

def encipher(plaintext):
    
    bacon_map = {

        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 
        'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
        'I': 'ABAAA', 'J': 'ABAAB', 'K': 'ABABA', 'L': 'ABABB',
        'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA', 'P': 'ABBBB', 
        'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 
        'Y': 'BBAAA', 'Z': 'BBAAB'
    }

    ciphertext = ''
    for i in plaintext.upper():
        if i in bacon_map:
            ciphertext += bacon_map[i]
    
    return ciphertext

def decipher(ciphertext):
    
    bacon_reversed = {

        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 
        'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 
        'ABAAA': 'I', 'ABAAB': 'J', 'ABABA': 'K', 'ABABB': 'L', 
        'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O', 'ABBBB': 'P', 
        'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
        'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X',
        'BBAAA': 'Y', 'BBAAB': 'Z'
    }

    plaintext = ''
    i = 0

    while i < len(ciphertext):

        x = ciphertext[i:i+5]
        if x in bacon_reversed:
            plaintext += bacon_reversed[x]
        i += 5

    return plaintext

def main():
    plaintext = 'MACARONI'
    ciphertext = encipher(plaintext)
    print("({}) {} : {}".format(plaintext, ciphertext, decipher(ciphertext)))
    

if __name__ == '__main__':
    main()