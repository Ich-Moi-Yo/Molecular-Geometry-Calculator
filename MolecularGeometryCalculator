"""
This first code delivery had the purpose of creating functions that with, some of the elements on the periodic table,
could show the ammount of electrons and protons of the element, its electron configuration or theyre noble gas configuration.

In future code deliverys more functions will be added to add further difficulty and purpose to the project.

"""



def electrons(e):
    print("Number of electrons and protons: ")
    if e == "H":
        return 1
    elif e == "He":
        return 2
    elif e == "Li":
        return 3
    elif e == "Be":
        return 4
    elif e == "B":
        return 5
    elif e == "C":
        return 6
    elif e == "N":
        return 7
    elif e == "O":
        return 8
    elif e == "F":
        return 9
    elif e == "Ne":
        return 10
    elif e == "Na":
        return 11
    else:
        return "Not"
    
    
    
def econfig(result):
    print("Electron configuration: ")

#H, He
    if result == 1 or result <= 2:
        if result == 1:
            return "1s1"
        else:
            return "2s2"

#Li, Be
    elif result == 3 or result <= 4:
        if result == 3:
            return "1s2, 2s1"
        else:
            return "1s2, 2s2"

#B, C, N, O, F, Ne
    elif result >= 5 and result <= 10:
        if result == 5:
            print("1s2, 2s2, 2p1")
        
        elif result == 6:
            print("1s2, 2s2, 2p2")
        
        elif result == 7:
            print("1s2, 2s2, 2p3")
            
        elif result == 8:
            print("1s2, 2s2, 2p4")
            
        elif result == 9:
            print("1s2, 2s2, 2p5")
            
        elif result == 10:
            print("1s2, 2s2, 2p6")
        
        elif result == 11:
             print("1s2, 2s2, 2p6, 3s1")
        
    else:
        return "Not"
        

#add elif for every case
    
    
def noble(result):
    print("Noble gas configurtion: ")
    
#H, He
    if result == 1 or result <= 2:
        if result == 1:
            return "1s1"
        else:
            return "[He]"
#Li, Be       
    elif result == 3 or result <= 4:
        if result == 3:
            return "[He]2s1"
        else:
            return "[He]2s2"
        
#B, C, N, O, F, Ne
    elif result >= 5 and result <= 10:
        if result == 5:
            print("[He]2s2, 2p1")
        
        elif result == 6:
            print("[He]2s2, 2p2")
        
        elif result == 7:
            print("[He]2s2, 2p3")
            
        elif result == 8:
            print("[He]2s2, 2p4")
            
        elif result == 9:
            print("[He]2s2, 2p5")
            
        elif result == 10:
            print("[Ne]")
            
    elif result >= 10 and result <= 12:
            
        if result == 11:
              print("[Ne]3s1")
              
        else:
            print("error")
            
    else:
        return "Not"
 

def menu():
    print("Choose an option:\n")
    print("1. Number of electrons and protons")
    print("2. Electron configuration")
    print("3. Noble gas configuration")
    print("4. Exit")

    return int(input("Option"))

    
def main():
    option = menu()

    if option == 1:
        e = str(input("e"))
        result = electrons(e)
        print(int(result))
        
    elif option == 2:
        e = str(input("e"))
        result = electrons(e)
        print(int(result))
        
        result = econfig(result)
        print(result)
        
    elif option == 3:
        e = str(input("e"))
        result = electrons(e)
        print(int(result))
        
        result = noble(result)
        print(result)
    
    elif option == 4:
        print("Exit")
        
    else:
         print("Error")

main()




#1s 2, 2s2, 2p6, 3s2, 3p6, 4s2, 3d10, 4p6, 5s2, 4d10, 5p6, 6s2, 4f14, 5d10, 6p6,7s2, 5f14, 6d10, 7p6
