# Molecular-Geometry-Calculator
This tool will allow you to enter the name of a compond and the program will tell you the name of its molecular geometry.

Algorithm:
  Input: Compond/molecule. Example: H2O
  Process: 
    - Ask user for compound/molecule
    - Identify elements present
    - Identify ammount of valance electrons (use electron configuration) per element and the ammount of atoms per element
    - Calculate total valance electrons
    - Calculate Octet electrons 
    - Calculate number of bonds (Oe - Ve)/2
    - Calculate nonebonding electrons
    - Calculate bonding pairs, lone pairs and total electron groups
    - Compare data to known characteristics of electron and molecular geometry
    - Print Molecular and electron geometries
    Output: Molecular and electron geometries




1st delivery:

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
