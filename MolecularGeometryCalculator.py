'''
                                        Molecular-Geometry-Calculator
                                    Demian Rohlfs Schondube - A01709641
                                    
This project was inspired by a chemistry class where once again I was faced with a bit of a tedious task, finding the
Molecular Geometry of compounds. This is a fairly simple thing to do, but it gets old quite quick when every exercise
starts with defining it. Also its just time consuming and boring when you already know exactly how to do it. So to
make the process of finding these geometry´s more efficient, this program was created.

It´s devided in 4 functions, The first three functions allow the user to find a compounds Molecular Geometry. To do this
the function 1. Total Bonds is called to calculate the ammount of bonds found in the compound. Then the function 2. Lone Pairs
is called to, in case there is a central atom, find how many unbonded electrons or lone pairs it has. Lastly the function
3. Molecular Geometry and Bond Angle is called to analyse through the set of data, found in MolecularG.txt, to determine
which condition is met by the compound and determine its Molecular Geometry and bond angle.

The calculation of the molecular geometry could have been bound together into one function, although it seemed sensible at first
it was decided to separate it in case the user wished to use the program to study. This way the final result would only appear in
the shell if the third function was called.

A fourth function was created to encapsulate useful information about the elements included in this first version of the program.
These elements are, Hydrogen, Helium, Lithium, Berylium, Boron, Carbon, Nitrogen, Oxigen, Flourine and Neon.

The program has certain limitations as to what compounds molecular geometry it can determine. This is due to the fact
that the databases cover until the tenth element of the periodic table. Also, this first version of the program is unable
to analyse compounds with double or triple bonds correctly. There are multiple areas of oportunity for the next version,
apart from the two already mentioned, some other areas of improvement are, the ammount of inputs the user must write and further
functions should be added to allow the user to obtain more information about the element or compound they wish to analyse.

Over all Test cases for the program, to attein the different results:

H2: 1,0,Linear,180° 
BeF2: 2,0,Linear,180°
H2O: 2,2,Bent,less than 109.5° 
BF3: 3,0,Triagonal Planar,120° 
NH2F: 3,1,Triagonal Pyramidal,less than 109.5° 
CH4: 4,0,Tetrahedral,109.5° 
'''

'''
Input:
   telements.txt

Process:
    readFileToMatrix() opens the file "telements.txt" to read, takes the pointer to the first position,
    reads the file line by line and closes the file. The file is cleaned using rstrip to elimintate the
    empty space on the right. Then split is used to separate the data with a certain character, in this
    case ";".
    
Output:
    IE:
    [['H; 1; 1; 2; 1s1; 1s1'], ['He; 2; 2; 2; 1s2; [He]'], ['Li; 3; 1; 2; 1s2', ' 2s1; [He]', ' 2s1'],
    ['Be; 4; 2; 4; 1s2', ' 2s2; [He]', ' 2s2'], ['B; 5; 3; 6; 1s2', ' 2s2', ' 2p1; [He]', ' 2s2', ' 2p1'],
    ['C; 6; 4; 8; 1s2', ' 2s2', ' 2p2; [He]', ' 2s2', ' 2p2'], ['N; 7; 5; 8; 1s2', ' 2s2', ' 2p3; [He]', ' 2s2', ' 2p3'],
    ['O; 8; 6; 8; 1s2', ' 2s2', ' 2p4; [He]', ' 2s2', ' 2p4'], ['F; 9; 7; 8; 1s2', ' 2s2', ' 2p5; [He]', ' 2s2', ' 2p5'],
    ['Ne; 10; 8; 8; 1s2', ' 2s2', ' 2p6; [Ne]']]
'''
def readFileToMatrix():
    file = open("telements.txt", "r+")
    file.seek(0)
    IE = file.readlines()
    file.close()
    for i in range(len(IE)):
        IE[i] = IE[i].rstrip().split(";")
    return IE


'''
Input:
   IE, element, pos
   
Process:
    It recives the matrix IE from readFileToMatrix(), the element from the user and pos or the position
    is hardcoded depending on which value is needed in the function to carry out the calculations. If the
    first value of a line or IE[i][0] corresponds to the element the user has given it will attach that
    value to the variable val.
    
Output:
    val
    
Test case:
    Input:
        element = H
        Valance = int(readIE(IE, element, 2))
    Output:
        Valance = 1      
'''
def readIE(IE, element, pos):
    val = 0
    for i in range(len(IE)):
        if (IE[i][0] == element):
            val = IE[i][pos]
    return val


'''
Input:
   MolecularG.txt

Process:
    readFileToMatrix2() opens the file "MolecularG.txt" to read, takes the pointer to the first position,
    reads the file line by line and closes the file. The file is cleaned using rstrip to elimintate the
    empty space on the right. Then split is used to separate the data with a certain character, in this
    case ";".
    
Output:
    MG:
    [['1', '0', 'Linear', '180 degrees'], ['2', '0', 'Linear', '180 degrees'],
    ['2', '2', 'Bent', 'less than 109.5 degrees'], ['3', '0', 'Triagonal Planar', '120 degrees'],
    ['3', '1', 'Triagonal Pyramidal', 'less than 109.5 degrees'], ['4', '0', 'Tetrahedral', '109.5 degrees']]
'''
def readFileToMatrix2():
    file = open("MolecularG.txt", "r+")
    file.seek(0)
    MG = file.readlines()
    file.close()
    for i in range(len(MG)):
        MG[i] = MG[i].rstrip().split(",")
    return MG


'''
Input:
   MG, bonds, LonePairs
   
Process:
    It recives the matrix MG from readFileToMatrix2(), the element from the user, the ammount of bonds is given as a
    global variable once Total_Bonds(IE) has been run and LonePairs is given as a global variable once Lone_Pairs(CVe) has been run.
    If the values MG[i][0] and MG[i][1] correspond to bonds and LonePairs val1 will be returned to the main.
    Where val1 = MG[i][2], MG[i][3] or Molecular Geometry and bond angle.
     
Output:
    val1
    
Test case:
    It is important to mention that in this function the values have not been converted to strings yet,
    This will happen in Molecular_Geometry(MG). But for this test case we will assume they are strings
    Input:
        bonds = '2'
        LonePairs = '2'
        
    Output:
        ('Bent', 'less than 109.5 degrees')      
'''
def readMG(MG, bonds, LonePairs):
    val1 = None
    for i in range(len(MG)):
        if (MG[i][0] == bonds) and (MG[i][1] == LonePairs):
            val1 = MG[i][2], MG[i][3]     
    return val1


'''
Input:
      IE, element, answer, n
   
Process:
    First the element is asked for, then n or the times the element is present in the compound,
    then the answer which corresponds if there are any other elements in the compound, if the answer
    is yes the last steps will be repeated. If the answer is no the ammount of bonds will be calculated
    using readIE to find the specific value needed in the matrix.
    As the inputs are given there will be results like the Valance electrons and Octet electrons
    counted up untill that moment, this is to maintain control and give the user extra information that helps
    to understand how the calculation is done.
     
Output:
    bonds
    
Test case:
    Input:
        element = H
        n = 2
        answer = yes
        
        proces is repeated
        
        element = O
        n = 1
        answer = no
        
    Output:
    
        Element in compound: H
        Valance electrons: 1
        Full shell: 2
        How many times is the element present?2
        Are there any more elements in the compound (Yes/No)?yes
        Total Valance electrons 2
        Total Octet electrons 4
        Element in compound: O
        Valance electrons: 6
        Full shell: 8
        How many times is the element present?1
        Are there any more elements in the compound (Yes/No)?no
        Total Valance electrons 8
        Total Octet electrons 12
        Total Bonds in compound: 2.0
         
'''
def Total_Bonds(IE):
    Ve = 0
    Oe = 0
    answer = "Yes"
    while answer == "Yes" or answer == "yes":
            
        element = str(input("Element in compound: "))
        if element and element[0].islower():
            print("Error: the first character is not uppercase.")
            break
        Valance = int(readIE(IE, element, 2))
        Octet = int(readIE(IE, element, 3))
        print("Valance electrons:", Valance)
        print("Full shell:", Octet)
        
        n = int(input("How many times is the element present?"))
        answer = str(input("Are there any more elements in the compound (Yes/No)?"))
        
        Oe = (Octet * n) + Oe
        Ve = (Valance * n) + Ve
        print("Total Valance electrons", Ve)
        print("Total Octet electrons", Oe)
    global bonds
    bonds = (Oe - Ve) / 2  
    return bonds

'''
Input:
    answer, element
    
Process:
    Fisrt it is asked if the compound has a central atom, if the answer is no the defoult
    paramenters are printed Molecular Geometry: MG[0][2] and Bond angle: MG[0][3] which
    constiitute to all posible compounds without central atom.
    If the answer is yes, the central atom is asked, from here CVe, or Central atom valance
    electrons, will be definded by reading the matrix and finding the elements valance electrons.
    Then the LonePairs are calculated and returned to the main.
    
Output:
    LonePairs
    
Test case:
    Input:
        answer = yes
        element = O
        
    Output:
        Is there a central atom?yes
        What element is the compounds central atom?O
        2.0       
'''
def Lone_Pairs(CVe):
    global LonePairs
    LonePairs = (CVe - bonds) / 2
    return LonePairs

'''
Input:
    MG, bonds, LonePairs
    
Process:
    bonds and LonePairs are converted to integers and then strings, to eliminate the float
    values created from calculations and assimilate with the string values in the matrix.
    Then the function readMG is called to see if any of the lines corresponds to the combination
    of bonds and lone pairs.
    If one correspondes and theres been no input error by the user the Molecular Geometry: values_MG[0]
    Bond angle: values_MG[1] will be printed.
    If the user inputs are incorrect a set of error posibilities will be displayed.
    
Output:
    Molecular Geometry: values_MG[0]
    Bond angle: values_MG[1]
      
Test case:
    Input:
        MG
         
    Output:
        Molecular Geometry: Bent
        Bond angle: less than 109.5 degrees
              
'''
def Molecular_Geometry(MG):
    SIbonds = str(int(bonds))
    SILonePairs = str(int(LonePairs))
    values_MG = readMG(MG, SIbonds, SILonePairs)
    
    
    if values_MG is not None:
        print("Molecular Geometry:", values_MG[0])
        print("Bond angle:", values_MG[1])
        
    else:
        print("Error Posibilities:")
        print(" 1.Incorrect input")
        print(" 2. The compoud you are trying to analyse does not exist")
        print(" 3. Element not found in Version 1 Database")
        print("	Elements in Databese, H, He, Li, Be, B, C, N, O, F and Ne")  #More elements will be added in future versions
        
'''
Input:
    opt
    
Process:
    All options are printed, signaling the numbers that correspond to each function.
    
Output:
        Molecular Geometry:
     1. Total Bonds
     2. Lone Pairs
     3. Molecular Geometry and Bond Angle

    Other functions:
     4. General Information about Element
'''      
def menu():
    print("Molecular Geometry:")
    print(" 1. Total Bonds")
    print(" 2. Lone Pairs")
    print(" 3. Molecular Geometry and Bond Angle")
    print()
    print("Other functions:")
    print(" 4. General Information about Element")
    print(" 5. Exit")
    
'''
Input:
    opt

Process:
    A opt value is given by the user and the corresponding code will be run.

Output:
    Depending on the function the return value given by the function, printed in the main.
    
All data capture was made in the main appart from the data capture done inside a while loop
as it was not posible to run the loop and capture the data if these where in a different positions. 
'''
def main():
    global IE
    IE = readFileToMatrix()
    global MG
    MG = readFileToMatrix2()
    while True:
        menu()
        opt = int(input("Option"))
    
        if opt == 1:
            print("This is the first step to find a compounds Molecular Geometry")
            result = Total_Bonds(IE)
            print("Total Bonds in compound:", result)
            
        elif opt == 2:
            print("This is the second step to find a compounds Molecular Geometry,\n"
            "remember, to use this function it is necesary to complete step one first.")
            answer = str(input("Is there a central atom?"))
            if answer == "Yes" or answer == "yes":
                element = str(input("What element is the compounds central atom?"))
                if element and element[0].islower():
                    print("Error: the first character is not uppercase.")
                    break
                CVe = int(readIE(IE, element, 2))
              
            else:
                print("Molecular Geometry:", MG[0][2])
                print("Bond angle:", MG[0][3])
                break
                    
            result = Lone_Pairs(CVe)
            print(result)
            
        elif opt == 3:
            print("")
            Molecular_Geometry(MG)
            
        elif opt == 4:
            element = input("What element would you like to analyse?")
            if element and element[0].islower():
                print("Error: the first character is not uppercase.")
                break
            
            ES = readIE(IE, element, 0)
            AN = readIE(IE, element, 1)
            Ve = readIE(IE, element, 2)
            Oe = readIE(IE, element, 3)
            EC = readIE(IE, element, 4)
            NGC = readIE(IE, element, 5)

            print("Element Symbol: ",ES)
            print("Atomic Number: ",AN)
            print("Valance electrons: ",Ve)
            print("Full shell: ",Oe)
            print("Electron Configuration: ",EC)
            print("Noble Gas Configuration: ",NGC,"\n")
            
        elif opt == 5:
            print("Goodbye")
            
        else:
            print("Error: Invalid input")
            
main()
