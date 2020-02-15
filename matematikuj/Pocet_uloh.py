
"""
Program zjistí počet úloh v jednotlivých tématech, které následně vytiskne do souboru,
Ze souboru si je pak nahraje view, které jej vypíše do buttonu spolu s názvem tématu
"""
import sys


soubor = open('static/pocet_uloh.txt',"w")
pocet = 0
for tema in sys.argv[2]:
    for priklad in sys.argv[1]:
        if priklad.tema == tema:
            pocet += 1
    print(tema)
    print(pocet)
    soubor.writelines([tema,pocet])
    pocet = 0
soubor.close()

    

