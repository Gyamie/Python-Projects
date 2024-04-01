#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = ''
for letter in range(1, nr_letters+1):
 diff_lett = random.choice(letters)
 password += diff_lett

for sym in range(1,nr_symbols+1):
  diff_sym = random.choice(symbols)
  password += diff_sym

for num in range(1, nr_numbers+1) :
   diff_num = random.choice(numbers)
   password +=  diff_num

password_mix = list(password)
random.shuffle(password_mix)
password_fin = ''.join(password_mix)

print(password_fin)

F_Input = input('please enter your first name\n').lower()
L_nput2 = input('please enter your last name\n').lower()

def format_name(F_name, L_name):
    print(F_name.capitalize())
    print(L_name.capitalize())

format_name(F_Input, L_nput2) 
