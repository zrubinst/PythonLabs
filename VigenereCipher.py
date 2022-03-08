# Assignment 1: Vigenere Cipher
# Zoe B. Rubinstein


# Generate key that is as long as the plaintext
def build_key(plaintext, key): 
    if len(plaintext) <= len(key):
        long_key = key
    elif len(plaintext) > len(key):
        long_key = key * (len(plaintext) // len(key) + 1)
    return long_key

# string of letters for indexing (ABCs)
letters = 'abcdefghijklmnopqrstuvwxyz'

# Function to encrypt
def encrypt(plaintext, key):
    long_key = build_key(plaintext, key) # extend key to length of plaintext
    encrypted = ''
    # loop to build encrypted text one letter at a time
    for i in range(len(plaintext)):
        index_plaintext = letters.find(plaintext[i]) # get index of given plaintext letter
        key_shift = letters.find(long_key[i]) # find index of corresponding key letter
        # encrypt plaintext items that are letters, leave non-letters as they were in plaintext
        if plaintext[i].isalpha():
            encrypted += letters[(index_plaintext + key_shift) % len(letters)]
        else: 
            encrypted += plaintext[i]    
    return encrypted

# Function to decrypt
def decrypt(encrypted_text, key):
    long_key = build_key(encrypted_text, key) # extend key to length of encrypted text
    decrypted = ''
    # loop to decrypt text one letter at a time
    for i in range(len(encrypted_text)):
        index_encrypt = letters.find(encrypted_text[i]) # get indext of given encrypted_text letter
        key_shift = letters.find(long_key[i]) # find index of corresponding key letter
        # decrypt encrypted text items that are letters by shifting in inverse direction using key
        if encrypted_text[i].isalpha():
            decrypted += letters[(index_encrypt - key_shift) % len(letters)]
        else:
            decrypted += encrypted_text[i]
    return decrypted

# Main function        
def main():
    plaintext = input('What is your message? ').lower() # ask for message
    print('Plaintext: ' + plaintext)
    key = input('Please enter a key: ') # ask for key
    # check that key only includes letters
    while not key.isalpha():
        key = input('Key must only contain letters. Please enter new key: ')
    # Encrypt, decrypt, and print
    encrypted_text = encrypt(plaintext, key)
    decrypted_text = decrypt(encrypted_text, key)
    print('Encrypted text: ' + encrypted_text)
    print('Decrypted text: ' + decrypted_text)
    

main()