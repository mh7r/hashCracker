from termcolor import colored
import hashlib
import sys
if len(sys.argv) != 4:
    print(colored("--------------------------", "green"))
    print(colored("Programin kullanimi:","blue"))
    print(colored("python md5cracker.py hash wordlist.txt hashlib"))
    print(colored("--------------------------", "green"))
    quit()
def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, "r")
    except:
        print(colored("[!!] Boyle bir dosya bulunamadi...)", "red"))
        quit()
hashGir = sys.argv[1]
wordlist = sys.argv[2]
hashLib = sys.argv[3]
tryOpen(wordlist)
if hashLib == "md5":
    a=0
    for word in pass_file:
        hashjob = hashlib.md5()
        hashjob.update(word.strip("\n").encode())
        hashim = hashjob.hexdigest()
        if hashim == hashGir:
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            print(colored("Hash basariyla kirildi...","yellow"))
            print(colored(f"{word}","yellow"), end="")        
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            a=1
            break
    if a == 0:
        print(colored("--------------------------", "green"))
        print(colored("Malesef bulamadim, baska wordlist deneyiniz...", "red"))
        print(colored("--------------------------", "green"))
elif hashLib == "sha1":
    a=0
    for word in pass_file:
        hashjob = hashlib.sha1()
        hashjob.update(word.strip("\n").encode())
        hashim = hashjob.hexdigest()
        if hashim == hashGir:
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            print(colored("Hash basariyla kirildi...","yellow"))
            print(colored(f"{word}","yellow"), end="")        
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            a=1
            break
    if a == 0:
        print(colored("--------------------------", "green"))
        print(colored("Malesef bulamadim, baska wordlist deneyiniz...", "red"))
        print(colored("--------------------------", "green"))
elif hashLib == "sha256":
    a=0
    for word in pass_file:
        hashjob = hashlib.sha256()
        hashjob.update(word.strip("\n").encode())
        hashim = hashjob.hexdigest()
        if hashim == hashGir:
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            print(colored("Hash basariyla kirildi...","yellow"))
            print(colored(f"{word}","yellow"), end="")        
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            a=1
            break
    if a == 0:
        print(colored("--------------------------", "green"))
        print(colored("Malesef bulamadim, baska wordlist deneyiniz...", "red"))
        print(colored("--------------------------", "green"))
elif hashLib == "sha512":
    a=0
    for word in pass_file:
        hashjob = hashlib.sha512()
        hashjob.update(word.strip("\n").encode())
        hashim = hashjob.hexdigest()
        if hashim == hashGir:
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            print(colored("Hash basariyla kirildi...","yellow"))
            print(colored(f"{word}","yellow"), end="")        
            print(colored("!!!!!!!!!!!!!!!!!!!!!!!!!!!!","cyan"))
            a=1
            break
    if a == 0:
        print(colored("--------------------------", "green"))
        print(colored("Malesef bulamadim, baska wordlist deneyiniz...", "red"))
        print(colored("--------------------------", "green"))
