from Crypto.Cipher import DES3
from hashlib import md5

# Prompt user to choose between encryption and decryption operations
while True:
    print('Choose operation to be done:\n\t1- Encryption\n\t2- Decryption')
    operation = input('Your Choice: ')
    if operation not in ['1', '2']:
        break

    # Request the file path for the operation
    file_path = input('File path: ')
    
    # Request the Triple DES key from the user
    key = input('TDES key: ')

    # Generate a 16-byte ASCII key using MD5 hashing
    key_hash = md5(key.encode('ascii')).digest()

    # Adjust the key parity for Triple DES compatibility
    tdes_key = DES3.adjust_key_parity(key_hash)
    
    # Create a cipher object using Triple DES key, MODE_EAX for Confidentiality & Authentication,
    # and nonce for generating a random or pseudo-random number used in the authentication protocol
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')

    # Open and read the file from the specified path
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()
        
        if operation == '1':
            # Encrypt the file contents
            new_file_bytes = cipher.encrypt(file_bytes)
        else:
            # Decrypt the file contents
            new_file_bytes = cipher.decrypt(file_bytes)
    
    # Write the updated values back to the file at the specified path
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        print('Operation Done!')
        break