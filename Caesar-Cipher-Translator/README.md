# Caesar-Cipher-Translator

Welcome to the Caesar Cipher project! This Python script allows you to encrypt and decrypt messages using the Caesar cipher algorithm. Below is a brief overview of the project and instructions on how to use it:

## Overview
The Caesar Cipher is a simple encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, 'a' would be replaced by 'b', 'b' would become 'c', and so on. The shift value wraps around the alphabet, so 'z' becomes 'a'.

## How to Use
1. Run the Python script in your preferred Python environment.
2. Choose whether you want to encrypt or decrypt a message by typing 'encode' or 'decode' when prompted.
3. Enter your message when prompted.
3. Specify the shift value (number of positions to shift each letter in the alphabet).
4. The script will then output the encrypted or decrypted message.
     
   Example

       Type 'encode' to encrypt, type 'decode' to decrypt:
       encode
       Type your message:
       hello
       Type the shift number:
       3
       the encoded text is khoor
    
## Note
1. The shift value should be a positive integer.
2. The script handles both uppercase and lowercase letters, as well as non-alphabetic characters, preserving their original positions in the message.
