#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#random.shuffle(x)
#random.choice
import random 
total_char = nr_letters + nr_numbers + nr_symbols
chosen_letters = []
for selected_letters in range(0,nr_letters):
  random_number = random.randint(0,51)
  random_letter = letters[random_number]
  chosen_letters+= random_letter

chosen_symbols = []
for selected_symbols in range(0,nr_symbols):
  random_symbol_number = random.randint(0,8)
  random_symbol = symbols[random_symbol_number]
  chosen_symbols += random_symbol

chosen_numbers = []

for selected_numbers in range(0,nr_numbers):
  random_number_number = random.randint(0,9)
  random_number_num = numbers[random_number_number]
  chosen_numbers += random_number_num

password = chosen_symbols + chosen_letters + chosen_symbols

for i in range(total_char):
  password_mixed = random.sample(password, total_char-1)
password_presented = ''.join(password_mixed)
print(f"Your password is {password_presented}")
