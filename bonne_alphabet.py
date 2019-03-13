import random
import copy as cp


#!/usr/bin/env python3
# -*- coding: utf-8 -*-



################ Question 1 : nombre min d'inversions #############################

def Inversion(L):
    """ inverse une liste de caractères"""
    Lc=cp.deepcopy(L)
    return Lc[::-1]

def ConvertAsci(L):
    """ convert to ascii code a list of characters"""
    La = []
    for i in range(len(L)):
        La.append(ord(L[i]))
    return La

#def FinOrdreAlphab(L):
#    """ Trouve la position de la première lettre qui n'est plus consécutive dans l'ordre alphabétique"""
#    La = ConvertAsci(L) # convertit la liste de caractère en liste de code ascii corespondant
#    
        

def Adjacent(L ):
    """ trouver les couples lettres de la liste de caractères convertis en code ascii L qui sont consécutives dans l'ordre alphabétique"""
    adj=[] # liste des indices des groupes adjacents
    for i in range(len(L)-1):
        if L[i]==L[i+1]+1 :
            adj.append([i, i+1])
        elif L[i]==L[i+1]-1:
            adj.append([i,i+1])
    return adj

def Score(L):
    """ calcul le nombre de couples de lettres qui sont consécutives dans l'ordre alphabétiques + si le min(L) est en position 0 + si le max(L) est en position -1.
    L est une liste de caractères convertis en code ascii"""
    score=len(Adjacent(L))
    if L.index(min(L))==0:
        score+=1
    if L.index(max(L))==len(L)-1:
    	
        score+=1
    return score


def end_ord(l) :
	"""prend en argument une liste de codes ASCII et renvoie l'indice de la première lettre qui n'est plus dans l'ordre alphabetique"""
	ind=0
	while l[ind+1]==l[ind]+1:
		if ind < len(l):
			ind+=1
	if ind ==0 : # La première lettre est mal placée
		return 0
	else :
		return ind+1


def nb_inversion(l):
	""" prend en argument une liste de chaine de caractères composées de lettre de l'alphabet retourne
	 le nobre minimum d'inversions necessaires pour obtenir une liste dans m'ordre alphabetique"""

	if isinstance(l, str):
		l_ascii= ConvertAsci(l) #converti en liste de code ascii
	else:
		l_ascii = l
	s=Score(l_ascii) #score initial de la sequence
	l_nb_inv = [] # Liste du nombre d'inversion nécessaire par "branche"
	d = 0
	P  = permutation(l_ascii , s , d ) # Stack 
	print("Permutation initile : ", P)
	nb_inv = 0

	while len(P) != 0 : # Tant que la pile n'est pas vide 
		nb_inv += 1 # On augmente le compteur pour la "branche" parcourue
		l_ascii = P[0][0] # On récupère le premier élement de la pile 
		s = P[0][1] # Score du premier elmt de la pile
		d = P[0][2] # Distance à l'origine du premier éléement de la pile

		if s!= len(l_ascii)+1  : # Si la seqence n'est pas triee
			
			p = permutation(l_ascii , s , d) # permutation du premier elmt
			P= P[1:] # Retire la permutation en cours de traitement 
			P = p+ P # Ajoute les résultats de "permutation" en tête de liste
		
		else : # On a finis de trier une "branche"
			l_nb_inv.append(P[0][2]) # On ajoute à la liste des résultats le nombre de permutation nécessaire pour obtenir un succes
			P= P[1:] # On enlève la permutation ayant conduit au succès
			#nb_inv = 0 # Et on réinitialise le score
		
	return min(l_nb_inv)



def permutation(liste_ascii, current_score, dist):
	"""Permutation prend en argument une liste d'entier correspondant au code ascii et le score associé à cette liste, et la distance de l'origine. 
	Cette fonction retourne une liste des permutations ayant permis d'améliorer ou de conserver le score pris en argument. """

	sorted_to =  end_ord(liste_ascii) # Retourne l'indice de la lettre qui n'est plus dans l'ordre
	Spe_cond = False # Utile pour la définition d'une condition (un peu tordue)

	if sorted_to != len(liste_ascii): # Vérifie si la liste est déjà triée
		min_letter= liste_ascii.index(min(liste_ascii[ sorted_to :])) # Renvoie l'indice de la plus petite lettre dans la séquence à trier 
		if sorted_to != min_letter : # Condition nécessaire pour dans le cas où le début de la séquence est déjà trié (Exemple : Mot2= "ABEDC")
			seq_to_permute =liste_ascii[ sorted_to :min_letter + 1]  # Recupération de la liste à permuter jusqu'à la lettre minimale incluse (+1)
		else : # Sinon  le début est incorrect
			if min_letter != 0: # Si la première n'est pas à la bonne position (Exemple : Mot1= "BCAED")
				seq_to_permute =liste_ascii[ : sorted_to  + 1]  # Récupéreration de la séquence jusqu'à la première incluse
			else : # Si la première lettre est bien placée et si seulement la première (Exemple : Mot3="ACBDFE")
				Spe_cond = True # Il y a exception (Condition spéciale = True)
				min_letter= liste_ascii.index(min(liste_ascii[ 1 :])) # Rechercher de la lettre minimale
				seq_to_permute =liste_ascii[ 1: min_letter + 1]   # La séquence est entre la deuxième lettre et la lettre minimale
	
		seq_after_permutation =[] # Liste des résultats d'une permuation 
		res = [] # Liste de toute les permutations admises

		for i in range(len(seq_to_permute)-1): # (-1) pour s'assurer que la séquence à inverser a une longueur supérieure à 1 
			seq_inv = Inversion(seq_to_permute[i:]) # Inversion de la séquence à permuter 

			if sorted_to != min_letter : # Dans le cas où le début de la séquence est déjà dans le bon ordre (Mot 2 et 3)
				if Spe_cond == False: # La lettre lettre minimale n'est pas la seule bien placée  (Mot 2)
					seq_after_permutation = liste_ascii[:sorted_to+i] +seq_inv + liste_ascii[min_letter+1:]
				else : # Sinon la condition spéciale est vraie (Mot 3)
					first_elmt = [liste_ascii[0]] # Nécessaire car sinon on traite un entier 
					seq_after_permutation = first_elmt+ seq_inv +  liste_ascii[min_letter+1:]

			else : # Si le début de la séquence n'est pas trié (Mot 1) 
				if len(seq_to_permute)== len(seq_inv): # Pour la première itération
					seq_after_permutation = seq_inv +liste_ascii[min_letter+1:]
				else : # Dans les cas suivants
					seq_after_permutation = liste_ascii[:len(seq_to_permute)-len(seq_inv)]+seq_inv+liste_ascii[min_letter+1:]

			c_score = Score(seq_after_permutation) # Calcul du nouveau score
	
			if c_score >= current_score: # Si on a une amélioration ou une égalité (C'EST JUSTE ÇA ???)
				res.append((seq_after_permutation , c_score , dist+1 )) # On retient la permutation			
		return res

	else: # Tout est déjà fait ;)
		print('The sequence is ever sorted') 
		return []	# On retourne une liste vide qui est nécessaire pour la gestion de la pile de la fonction (ou qui était nécessaire je sais plus)
			
def seq_aleatoire(l_ascii):
	"Permet de générer une séquence alétoire de même composition que celle passée en argument"
	random.shuffle(l_ascii)
	return l_ascii

def scenario_aleatoire(l,runs):
	"""Scenario aleatoire prend en argument une liste d'entier correspondant au code ascii d'une séquence
	et un nombre de simulations (runs). Cette fonction calcule le nombre d'inversions nécessaires
	pour trier une séquence aléatoire et retournera une liste contenant le nombre d'inversion minimal qui 
	a été nécessaire pour résoudre chaque simulation (séquence aléatoire), ainsi que le nombre d'inversion moyen. """

	res =[]
	for i in range(runs):
		print('i : ', i)
		L = seq_aleatoire(l)
		c_res = nb_inversion(L)
		res.append(c_res)
	moy_dist= sum(res)/len(res)
	return res, moy_dist

print("\n MOT 1  ")
mot1 = "bcaed" 
L1 = ConvertAsci(mot1)
P1  = permutation(L1, Score(L1), 0)
print("Adjacence L1  : ", Adjacent(L1))
print("Score  ", Score(L1))
print("Trie jusqu a : ", end_ord(L1))
print("Permutation P1 " , P1)


print("\n MOT 2  ")
mot2 = "abedc" 
L2 = ConvertAsci(mot2)
P2  = permutation(L2, Score(L2),0)
print("P2", P2)



print("\n MOT 3  ")
mot3 = "acbdfe" 
L3 = ConvertAsci(mot3)
print("Adjacence L3  : ", Adjacent(L3))
print("Score  ", Score(L3))
P3  = permutation(L3, Score(L3),0)
print("P3", P3)


print("\n MOT 3  ")
mot3 = "bcadfegih"
L3 = ConvertAsci(mot3)
print("TRie jusqua : ", end_ord(L3))
P3  = permutation(L3, Score(L3),0)
print("P1", P3)
print("\n")
print('\n  Nb inversion obs   :    \n' , nb_inversion("bcadfe")  )



print("\n MOT Exemple cours   ")
mot4 = "lhfebadckijgm"
L4 = ConvertAsci(mot4)
print("Trie jusqua : ", end_ord(L4))
P4  = permutation(L4, Score(L4),0)
print("P4", P4)

print('\n')
print('\n')
print('\n Nb inversion obs   :    \n' , nb_inversion("lhfebadckijgm")  )
print('\n scenario_aleatoire de L4  :',  scenario_aleatoire(L4,4)[0], 'Distance moy', scenario_aleatoire(L4,4)[1] )


# Un peu plus long 
print('\n')
mot5 = "ailgkjmbcefhd"
L5= ConvertAsci(mot5)
print("Trie jusqua : ", end_ord(L5))
P5 = permutation(L5, Score(L5),0)
print("P5", P5)
print('\n')
print('\n Nb inversion obs   :    \n' , nb_inversion("ailgkjmbcefhd")  )
