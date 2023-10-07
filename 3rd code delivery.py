"""
Este primer texto contiene:

    - Dudas que me surgieron mientras cambiaba if statements por matrices y listas
    - Posibles direcciones en las cuales mejorar el codigo
    - comentarios generales para recordar los problemas encontrados
    
    
Comence a intentar convertir las funciones en las que utiliso if statements a funcionar tomando los valores
de la matriz M para acortar el código.

Tengo algunas dudas que espero podamos analizar el lunes respecto a si es posible, para eficientar
la función atomicNumber(element) utilizando for loops, dandole un valor a cada elemento desde antes.
Llendo en esta dirección:
def atomicNumber(element):
    for i in range(len(M)):
        for j in range(len(M[i])):
    if element == "H":
        return(M[0][0])
        
Igualmente necesito encontrar la manera de crear funciones dentro de funciones, llendo haca esta dirección:
def atomicNumber(element):
    if element == "H":
        def menu():
            print("1. atomicNumber(element)  \n2. econfig(result)")
        def econfig():
            return(M[0][1])
            
            
        #return(M[0])
        
    elif element == "He":
        return(M[1])
    elif element == "Li":
        return(M[2])
    elif element == "Be":
        return(M[3])
    elif element == "B":
        return(M[4])
    elif element == "C":
        return(M[5])
        

Igualmente se añadieron los strings en atomicNumber para verificar que el usuario esta escribiendo
los nombres de los elementos correctamente, esto en la verion final sera un statement al inicio del main


"""

'''
The functions of this code are not yet completely finished, each one will give you the information
about the element its name states. The final function which by itself will be a compilation
of all the elements information is not yet defined, as first the code must migrate from
if statements to using matrices and lists
'''

M = [[1,"1s1","1s1"],[2,"1s2","[He]"],[ 3,"1s 2, 2s1", "[He]2s1"]]

def atomicNumber(element):
    if element == "H":
        return(M[0][0])
    elif element == "He":
        return(M[1][0])
    elif element == "Li":
        return(M[2][0])
    elif element == "Be":
        return(M[3][0])
    elif element == "B":
        return(M[4][0])
    elif element == "C":
        return(M[5][0])


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
    
    
def TotalVe(result,n):
    total = 0
    product = result * n
    #print("TotalVe for "e, result)
    """
    while True:
        answer = str(input("Are there any more elements in the compound?"))
        if answer == "Yes" or "yes":
            electrons(e)
            TotalVe()
            
            
            
       
       #while answer != "No" and answer != "no" and answer != "Yes" and answer != "yes":
       #     print("incorrect choice, Yes or No")
       #     answer = str(input("Are there any more elements in the compound?"))
        
        elif answer == "No" or answer == "no":
            total += product
            return total
            
    """
    return total
        
        
        
 

def menu():
    print("Choose an option:\n")
    print("1. Number of electrons and protons")
    print("2. Electron configuration")
    print("3. Noble gas configuration")
    print("4. TotalVe")
    print("5. Atomic Number(using matrix)")
    print("6. Exit")

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
       
        totalelectrons = 0
        answer = "Yes"
        while answer == "Yes" or answer == "yes":
            
            e = str(input("What element "))
            result = electrons(e)
            print(int(result))
        
            n = int(input("How many times is the element present?"))
            answer = str(input("Are there any more elements in the compound?"))
            
            
 
            
            totalelectrons = (result * n) + totalelectrons
            print(totalelectrons)
    
    elif option == 5:
          #string element of program
        element = input("What element do you want to analyse?")
        if element and element[0].islower():
            print("The first character is not uppercase.")
       
        
        #element = str(input("Element"))
        result = atomicNumber(element)
        print(result)
        
    elif option == 6:
        print("Exit")
        
    else:
         print("Error")

main()

