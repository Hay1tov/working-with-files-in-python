from colorama import Fore, Back, Style

print(f"{Style.DIM}nechta kontakt kiritmoqchisiz -> ", end = " ")
number = int(input())
s = 0
while s != number:
    if s == number:
        break
    
    print(f"{Style.BRIGHT} {Fore.BLUE}Ismni kiriting -> ", end = " ")
    name = input()
    print(f"{Style.BRIGHT} {Fore.BLUE}Telefon raqamni kiriting -> ", end = " ")
    phone_number = input()
    
    file = open("contact.txt", 'a')
    file.write(name)
    file.write(": ")
    file.write(phone_number)
    file.write("\n")
    file.close()
    f = open("contact.txt", 'r')
    print(f.read())
    
    s += 1
print(f"{Style.BRIGHT} {Fore.GREEN}exiting...")