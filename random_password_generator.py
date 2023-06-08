import os
import random

os.system('cls')
print("===============================")
print("||                           ||")
print("||    PASSWORD GENERATOR     ||")
print("||                           ||")
print("===============================")

def password_generator(length):
    password = ""
    if length < 8:
        print("\nLength too small to create Password")
        exit()
    elif length > 16:
        print("\nLength too big to create Password(Length out of Range)")
        exit()
    else:
        for i in range(random.choice(l)):
            password = password + random.choice(characters_Small)
        for i in range(random.choice(l)):
            password = password + random.choice(characters_Big)
        for i in range (random.choice(l)):
            password = password + random.choice(digits)
        for i in range(random.choice(l)):
            password = password+random.choice(special)
        len_pass = len(password)
        for i in range(length-len_pass):
            password = password + random.choice(all_characters)
        final_password = ''.join(random.sample(password, length))
        print(f"Here is your Password: {final_password}")
        

all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*-+~!@#$%^&()_={}|'?/><,.[\]"
characters_Small= "abcdefghijklmnopqrstuvwxyz"
characters_Big= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
special = "/*-+~!@#$%^&()_={}|'?/><,.[\]"
l = [1,2]
length = int(input("\nEnter the length of Password you want?\n>> "))
password_generator(length)

response = 'y'
while(response=='y'):
    regen = input("\nDo you want to regenrate the password?\n>>[y/n]: ")
    if regen.lower() == 'y':
        password_generator(length)
    elif regen.lower() == 'n':
        print("Thanks for using password Generator!! :)\nDont share your password with anyone...")    
        response = 'n'
    else:
        print("Thanks for using password Generator!! :)\nDont share your password with anyone...")    
        exit()