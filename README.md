# Molecular-Geometry-Calculator
This program allows you to input the name of a compound and it will tell you its molecular geometry, bond angle and useful information about elements such as Element Symbol, Atomic Number, Valance electrons, Full shell, Electron Configuration and Noble Gas Configuration.
This project was inspired by a chemistry class where once again I was faced with a bit of a tedious task, finding the Molecular Geometry of compounds. This is a fairly simple thing to do, but it gets old quite quick when every exercise starts with defining it. Also, its just time consuming and boring when you already know exactly how to do it. So, to make the process of finding these geometry´s more efficient, this program was created.
It´s divided in 4 functions, the first three functions allow the user to find a compounds Molecular Geometry. To do this the function 1. Total Bonds is called to calculate the amount of bonds found in the compound. Then the function 2. Lone Pairs is called to, in case there is a central atom, find how many unbonded electrons or lone pairs it has. Lastly the function 3. Molecular Geometry and Bond Angle is called to analyze through the set of data, found in MolecularG.txt, to determine which condition is met by the compound and determine its Molecular Geometry and bond angle.
A fourth function was created to encapsulate useful information about the elements included in this first version of the program. These elements are, Hydrogen, Helium, Lithium, Beryllium, Boron, Carbon, Nitrogen, Oxygen, Fluorine and Neon.
The program has certain limitations as to what compounds molecular geometry it can determine. This is due to the fact that the databases cover until the tenth element of the periodic table. Also, this first version of the program is unable to analyze compounds with double or triple bonds correctly. There are multiple areas of opportunity for the next version, apart from the two already mentioned, some other areas of improvement are, the amount of inputs the user must write and further functions should be added to allow the user to obtain more information about the element or compound they wish to analyze.


General Algorithm:
  Input: Compond/molecule. Example: H2O
  Process: 
    - Ask user for compound/molecule
    - Identify elements present
    - Identify amount of valance electrons (use electron configuration) per element and the ammount of atoms per element
    - Calculate total valance electrons
    - Calculate Octet electrons 
    - Calculate number of bonds (Oe - Ve)/2
    - Calculate lone pairs 
    - Compare data to known characteristics of electron and molecular geometry
    - Print Molecular  geometry
    Output: Molecular Geometry
    
