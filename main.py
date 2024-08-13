



import random 

print("hello \n")

print ("Here are the list of passwords!! \n")

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<\\"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
  all += uppercase_letters  
if lower:
  all += lowercase_letters  
if nums: 
  all += numbers
if syms:
  all += symbols

# lentgh of the passwords
length = 20
# amount of passwords generated
amount = 10

for x in range(amount):
  password = "".join(random.sample(all, length))
  print (password)
  print("\n\n")
  




