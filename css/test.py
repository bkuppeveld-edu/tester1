lijst = []
looper = True

while looper == True:
    input1 = input("Wat wil je toevoegen?")
    lijst.append(input1)
    for x in lijst:
        print(x)
    
    removeOption = input("Wil je iets verwijderen? y/n")
    if(removeOption == "y"):
        remove2 = input("Wat wil je verwijderen?")
        lijst.remove(remove2)
    else:
        print("oke")

    stop = input("wil je stoppen? y/n")
    if(stop == "y"):
        looper = False
    else:
        print("oke")

