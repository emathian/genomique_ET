mon_fichier=open("1348_chromosome.txt",'r')
sequence=mon_fichier.read()
taille=0
nbN=0
entree=False
for i in sequence :
    if entree==False :
        if i=='\n' :
            entree=True
    elif i=="A" or i=="T" or i=="c" or i=="G" or i=="N":
        taille+=1
        if i=="N" :
            nbN+=1
        #print (i)
print(taille, nbN)
mon_fichier.close()

# 1348_chromosome.txt : taille génome = 3533579 ; nb sites non def = 25769
