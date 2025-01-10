from os import system
from colorama import Fore, Style

system('clear')

count = int(input(f"{Style.DIM} {Style.BRIGHT}sotib olgan mahsulotlaringiz sonini yozing -> "))
s = 0
while s != count:
    if s == count:
        break
    product = input(f"{Style.BRIGHT} {Fore.BLUE}---Siz sotib olgan mahsulotingiz nomini kiriting -> ")
    
    file = open("shopping_list.txt", 'a')
    file.write(product)
    file.write("\n")
    file.close()
    f = open("shopping_list.txt", 'r')
    print(f.read())
    
    s += 1
print(f"{Style.BRIGHT} {Fore.GREEN}exiting...")