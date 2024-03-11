def criptare_vigenere(plaintext, key):
   text_criptat = ""
   lungime_cheie = len(key)


   for i in range(len(plaintext)):
       char = plaintext[i]
       if char.isalpha():
           key_char = key[i % lungime_cheie].upper()
           shift = ord(key_char) - ord('A')


           if char.islower():
               text_criptat += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
           elif char.isupper():
               text_criptat += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
       else:
           text_criptat += char


   return text_criptat




def decriptare_vigenere(ciphertext, key):
   text_decriptat = ""
   lunigme_cheie = len(key)


   for i in range(len(ciphertext)):
       char = ciphertext[i]
       if char.isalpha():
           key_char = key[i % lunigme_cheie].upper()
           shift = ord(key_char) - ord('A')


           if char.islower():
               text_decriptat += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
           elif char.isupper():
               text_decriptat += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
       else:
           text_decriptat += char


   return text_decriptat




def main():
   while True:
       print("1. Criptare")
       print("2. Decriptare")
       print("3. Exit")


       choice = input("Alegeti optiunea dorita:")


       if choice == "1":
           plaintext = input("Text pentru criptat: ")
           key = input("Cheia: ")
           encrypted_text = criptare_vigenere(plaintext, key)
           print("Textul criptat: ", encrypted_text)
       elif choice == "2":
           ciphertext = input("Text pentru decriptat: ")
           key = input("Cheia: ")
           decrypted_text = decriptare_vigenere(ciphertext, key)
           print("Textul decriptat: ", decrypted_text)
       elif choice == "3":
           break




if __name__ == "__main__":
   main()
