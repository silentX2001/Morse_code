#This Tool is Build By Rajdeep Ghosh
#It's for my MAR purpose 
import os , subprocess

#Declaration Of Morse code
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..','a':'.-', 'b':'-...',
   'c':'-.-.', 'd':'-..', 'e':'.',
   'f':'..-.', 'g':'--.', 'h':'....',
   'i':'..', 'j':'.---', 'k':'-.-',
   'l':'.-..', 'm':'--', 'n':'-.',
   'o':'---', 'p':'.--.', 'q':'--.-',
   'r':'.-.', 's':'...', 't':'-',
   'u':'..-', 'v':'...-', 'w':'.--',
   'x':'-..-', 'y':'-.--', 'z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

#Encrypter
def encryption(message):
   my_cipher = ''
   for myletter in message:
      if myletter != ' ':
         my_cipher += MORSE_CODE_DICT[myletter] + ' '
      else:
         my_cipher += ' '
      return my_cipher

#Decrypter 
def decryption(message):
   message += ' '
   decipher = ''
   mycitext = ''
   for myletter in message:
      # checks for space
      if (myletter != ' '):
         i = 0
         mycitext += myletter
      else:
         i += 1
         if i == 2 :
            decipher += ' '
         else:
            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
            .values()).index(mycitext)]
            mycitext = ''
   return decipher


def main():
   os.system("clear")
   print("Welcome To My Morse Code Translation Tool\n\n")
   print("Options :\n1. Text to Morse code\n2. Morse code to Text\n3. Credit\n")
   gbd = int(input("\nEnter selection : "))
   if gbd == 1:
       os.system("clear")
       print("Welcome To Encryption Mode\n\n")       
       my_message = str(input("Enter Your Text :\n"))
       output = encryption(my_message)
       print("\nHere is Your Morse Code of Your Text\n")
       print (output)
       print ("\n\n\nThanks For Using\n")
   elif gbd == 2:
       os.system("clear")
       print("Welcome To Deception Mode\n\n")       
       my_message = str(input("Enter Your Morse Code :\n"))
       output = decryption(my_message)
       print("\nHere is Your Decrypted Text\n")
       print (output)
       print ("\n\n\nThanks For Using\n")
   elif gbd == 3:
       os.system("clear")
       my_message = "- .... .. ...  - --- --- .-..  .. ...  -... ..- .. .-.. -..  -... -.--  .-. .- .--- -.. . . .--.  --. .... --- ... ...."
       output = decryption(my_message)
       print (output)
       os._exit(1)
   else:
       os.system("clear")
       print ("\nWrong Input\n\nThanks For Using\n")
       os._exit(1)

main()