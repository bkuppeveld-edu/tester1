lijst = []
looper = True
while looper == True:
    lijst.append(input("wat wil je meenemen?"))
    for x in lijst:
        print(x)
        
    remove = input("wat wil je eruit halen?")
    check = input("wil je nog meer toevoegen y/n")
    

    lijst.remove(remove)
    if (check == "n"):
        looper = False
    else:
        looper = True

