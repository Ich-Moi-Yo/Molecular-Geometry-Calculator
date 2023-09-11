


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
    
    
def TotalVe(compound):
    total = 0
    for element, count in compound.items():
        result = electrons(element)
        if result != 0:
            total += result * count
        else:
            print(f"Element {element} is not recognized. Please check the compound.")
    return total
                   
 

def menu():
    print("Choose an option:\n")
    print("1. Number of electrons and protons")
    print("2. Electron configuration")
    print("3. Noble gas configuration")
    print("4. TotalVe")
    print("5. Exit")

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
        compound = {}
        while True:
            element = str(input("Element in the compound, only one "))
            count = int(input(f"How many times is {element} present in the compound? "))
            compound[element] = count
            another_element = input("Do you want to add another element to the compound? (yes/no): ").lower()
            if another_element != 'yes':
                break
        
        total_valence = TotalVe(compound)
        print(f"Total valence electrons in the compound: {total_valence}")
            
        result = TotalVe(result,n)
        print(result)
    
    elif option == 5:
        print("Exit")
        
    else:
         print("Error")

main()


