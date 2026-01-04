import string
import random
a=""
total_length = int(input("Enter total password length: "))
num_digits = int(input("How many numbers  needed? "))
num_symbols = int(input("How many symbols needed? "))
letters = string.ascii_letters 
digits = string.digits        
symbols = string.punctuation   
if num_digits + num_symbols > total_length:
    print("Error")
else:
    for i in range(num_digits):
        a+=digits[random.randint(0,len(digits)-1)]
    for i in range(num_symbols):
        a+=symbols[random.randint(0,len(symbols)-1)]
    for i in range(total_length-(num_digits + num_symbols)):
        a+=letters[random.randint(0,len(letters)-1)]
    b=list(a)
    random.shuffle(b)
    print("")
    for i in b:
        print(i,end="")
    print("")
