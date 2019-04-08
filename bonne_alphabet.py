#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import division
import random
import copy as cp
import pandas as pd

################ Question 1 : nombre min d'inversions #############################

def inversion(L):
	"""Inverse les éléments d'une liste.

	Cette fonction permet de réecrire les éléments de `L` de
    droite à gauche.

    Parameters
    ----------
    L : list
        `L` est une liste ou une liste de liste.
	
    Returns
    -------
   Lc : array_like
    	`Lc` est équivalente à liste `L` lue de droite à gauqhe.   
	
    Examples
    --------
	>>> L = [1,2,3,4,5]
	>>> inversion(L)
	[5, 4, 3, 2, 1]

    """
	Lc = cp.deepcopy(L)
	return Lc[::-1]

def ConvertAsci(L): # e
    """Fonction qui convertie une liste de caracteres en liste de code ascii.

    Parameters
    ----------
    L
        Une liste de caracteres.

    Returns
    -------
    La
        Une liste de code ascii.

    """
    La = []
    for i in range(len(L)):
        La.append(ord(L[i]))
    return La

def adjacent(L): 
    """Recherche l'ensemble des éléments consécutifs d'une listes d'entiers.

    Cette fonction prend en argument une liste d'entiers et retourne 
    une liste de listes contenant tous les couples d'indices dont les 
    valeurs dans `L` sont consécutives selon l'ordre numétique. Une liste 
    vide est retournée si aucun élément de `L` n'est consécutif.

    Parameters
    ----------
    L : list
        `L` est une liste d'entiers.
	
    Returns
    -------
    adj : array_like
       	`adj` est liste de listes contenant de tous les couples d'indice
        de `L` dont les valeurs sont consécutives.   
	
    Examples
    --------
	>>> L1 = [3,4,1,2]
	>>> adjacent(L1)
	[[0, 1], [2, 3]]
	>>> L2 = [1,2,3,4]
	>>> adjacent(L2)
	[[0, 1], [1, 2], [2, 3]]
	>>> L3 = [2,4,1,3]
	>>> adjacent(L3)
	[]

    """
    adj=[] 
    for i in range(len(L)-1):
        if L[i]==L[i+1]+1 : 
            adj.append([i, i+1])
        elif L[i]==L[i+1]-1:
            adj.append([i,i+1])
    return adj

def score(L): # e
    """ calcul le nombre de couples de lettres qui sont consécutives dans l'ordre alphabétiques + si le min(L) est en position 0 + si le max(L) est en position -1.
    L est une liste de caractères convertis en code ascii"""
    score=len(adjacent(L))
    if L.index(min(L))==0:
        score+=1
    if L.index(max(L))==len(L)-1:
    	
        score+=1
    return score


def end_ord(l) : 
	"""Recherche l'indice du premier élément non trié

    Cette fonction recherche le premier élément d'une liste d'entiers 
    qui n'est pas dans l'ordre numérique et retourne son indice. Si la
    valeur retounée est égale à zéro alors les deux premiers éléments
    ne sont pas dans le bonne ordre, la suite des éléments étant possiblement
    triés. Si la valeur retournée est égale à la longueur de la liste,
    alors cele-ci est triée.  

    Parameters
    ----------
    l : list
        `l` est une liste d'entiers.

    Returns
    -------
    int
        Indice du premier élément mal positionné de `l`.
	
    See Also
    --------
    permutation : Recherche itérative de toutes les inversions permettant d'améliorer le score
    nb_inversion : Recherche itérative du nombre minimal d'inversion 
   
    Examples
    --------
	>>> L1 = [3,4,1,2]
	>>> end_ord(L1)
	2
	>>> L2 = [1,2,3,4]
	>>> end_ord(L2)
	4
	>>> L3 = [2,4,1,3]
	>>> end_ord(L3)
	0

    """
	ind=0
	cond = True
	while cond : 
		if ind < len(l) -1 :
			if l[ind+1]==l[ind]+1 :  # Si l'élément courrant +1 est équivalent au suivant. 
				ind+=1
				cond = True 
			else :
				cond = False
		else :  # La liste est entièrement triée.
			cond = False
	if ind ==0 : 
		return 0
	else :
		return ind+1

def nb_inversion(l, v2 = False): # e
	""" prend en argument une liste de chaine de caractères composées de lettre de l'alphabet retourne
	 le nobre minimum d'inversions necessaires pour obtenir une liste dans m'ordre alphabetique"""

	if isinstance(l, str):
		l_ascii= ConvertAsci(l) #converti en liste de code ascii
	else:
		l_ascii = l
	s=score(l_ascii) #score initial de la sequence
	l_nb_inv = [] # Liste du nombre d'inversion nécessaire par "branche"
	d = 0
	if v2 == False :
		P  = permutation(l_ascii , s , d ) # Stack 
	else :
		P = permutation_v2(l_ascii , s , d )
	nb_inv = 0

	while len(P) != 0 : # Tant que la pile n'est pas vide 
		nb_inv += 1 # On augmente le compteur pour la "branche" parcourue
		l_ascii = P[0][0] # On récupère le premier élement de la pile 
		s = P[0][1] # score du premier elmt de la pile
		d = P[0][2] # Distance à l'origine du premier éléement de la pile

		if s!= len(l_ascii)+1  : # Si la seqence n'est pas triee
			if v2 == False :
				p = permutation(l_ascii , s , d) # permutation du premier elmt
			else :
				p = permutation_v2(l_ascii , s , d)
			P= P[1:] # Retire la permutation en cours de traitement 
			P = p+ P # Ajoute les résultats de "permutation" en tête de liste
			
		else : # On a finis de trier une "branche"
			l_nb_inv.append(P[0][2]) # On ajoute à la liste des résultats le nombre de permutation nécessaire pour obtenir un succes
			P= P[1:] # On enlève la permutation ayant conduit au succès
			#nb_inv = 0 # Et on réinitialise le score
	
	if len(l_nb_inv) > 0 :
		min_nb_inv = min(l_nb_inv)
	else : # Aucune inversion n'a été nécessaire
		min_nb_inv = 0
	return min_nb_inv 


def permutation(L, score_courant, dist): 
	"""Recherche les inversions possibles permettant de conserver ou d'améliorer le score

    Cette fonction prend en argument une liste d'entiers, son `score_courant` 
    (cf : `score`), ainsi que sa distance à l'origine (à la séquence initiale). 
    En effet elle est appellée par la procédure `nb_inversion`, qui détermine
    le nombre d'inversions nécessaires pour trier une liste, ce nombre 
    d'inversions détermine la distance l'origine d'une possibilité.

   	Ainsi étant donné une liste et son état courant, `permutation` commence
   	par déterminer la séquence à inverser, si une inversion est nécessaire.
   	Pour `i` allant de 0 à la taille de la séquence à inverser -1, `permuatation`
   	genère l'inversion de taille `i`, et recalcul le score. Si celui-ci au 
   	moins égal au `score_courant`, `permutation` retient la liste inversée, 
   	son score et incrémente sa distance de 1.

    Parameters
    ----------
    L : list
        `L` est une liste d'entiers.
    score_courant : int
    	score de la liste (cf : `score`).
    dist :  int
		Distance à l'origine pour la séquence `L`, traduit le nombre d'inversions
		qui ont déjà été réalisées sur `L`.

    Returns
    -------
    res : liste de tuples
    	`res` est une liste contanant autant de tuple que d'inversions
    	conservées. Chaque tuple est constitué de la séquence après 
    	inversion, de son score et de sa distance (`dist` + 1).
	
    See Also
    --------
    nb_inversion : Recherche itérative du nombre minimal d'inversion 

	Notes
    -----
    Étant donné que cette fonction fait appel à `nb_inversion`, elle ne peut
    être appliquée que pour des listes de petite taille, afin de garantir 
    l'éxécution du calcul dans un temps raisonnable. 

    `permutation` gère les cas suivants :
    1 : Si `L` est déjà triée une liste vide est renvoyée.

    2 : Si seulement le début de `L` est trié la séquence à 
    inverser correspond aux éléments situés après le dernier
    élément dans le bon ordre. 
    Exemple : ABEDC -> Séquence à inverser = EDC

    3 : Si le début de la séquence n'est pas trié alors
    la séquence à inverser correspond à l'ensemble des éléments
    situés avant l'élément minimal.
    Exemple : EDABC -> Séquence à inverser = EDA

    4 : Si les premiers éléments de `L` sont successif mais
    si le premier élément n'est pas bien placé alors la séquence
    à inverser correspond à l'ensemble des éléments situés en 
    amont du premier élément.
    Exemple : BCAED -> Séquence à inverser = BCA

	5 :  Si la première lettre est bien placée et si seulement
	la première l'est alors la séquence à inverser correspond 
	aux éléments situés après le premier élément et l'élément
	minimal (sans prise en compte du premier).
	Exemple : ACBDFE -> Séquence à inverser = CB

   
    Examples
    --------
	>>> L1 = [1,2,5,4,3]
	>>> S1 = score(L1)
	>>> permutation(L1,S1,0)  # Cas n°2
	[([1, 2, 3, 4, 5], 6, 1)]
	>>> L2 = [5,4,1,2,3]  
	>>> S2 = score(L2)
	>>> permutation(L2,S2,0)  # Cas n°3
	[([1, 4, 5, 2, 3], 3, 1)]
	>>> L3 = [2,3,1,5,4]
	>>> S3 = score(L3)
	>>> permutation(L3,S3,0)  # Cas n°4
	[([1, 3, 2, 5, 4], 3, 1), ([2, 1, 3, 5, 4], 2, 1)]
	>>> L4 = [1,3,2,4,6,5]
	>>> S4 = score(L4)
	>>> permutation(L4,S4,0)  # Cas n°5
	[([1, 2, 3, 4, 6, 5], 5, 1)]

    """

	sorted_to =  end_ord(L)  # Retourne l'indice du premier élément qui n'est plus dans l'ordre
	Spe_cond = False  # Condition spéciale (cf : Cas n°5)

	if sorted_to != len(L):  # Cas n°1
		min_letter= L.index(min(L[ sorted_to :])) 
		if sorted_to != min_letter :  # Condition nécessaire pour dans le cas où le début de la séquence est déjà trié (Exemple : Mot2= "ABEDC") (Cas n°2 et n°3)
			seq_to_permute =L[ sorted_to :min_letter + 1]  # Recupération de la liste à permuter jusqu'à l'élément minimale inclus (+1)
		else :  # Cas n°4 et n°5
			if min_letter != 0:  # Si la première n'est pas à la bonne position (Exemple : Mot1= "BCAED") (Cas n°4)
				seq_to_permute =L[ : sorted_to  + 1]  # Récupéreration de la séquence jusqu'au premiere élément inclus
			else :  # Si la première lettre est bien placée et si seulement la première (Exemple : Mot3="ACBDFE") (Cas n°5)
				Spe_cond = True 
				min_letter= L.index(min(L[ 1 :])) # Redéfinition du minimum
				seq_to_permute =L[ 1: min_letter + 1] # La séquence est entre le deuxième élément et l'élément minimale
	
		seq_after_permutation =[]  # Liste des résultats d'une permuation 
		res = []  # Liste de toute les permutations admises

		for i in range(len(seq_to_permute)-1):  # (-1) pour s'assurer que la séquence à inverser a une longueur supérieure à 1 
			seq_inv = inversion(seq_to_permute[i:])  # inversion de la séquence à permuter 

			if sorted_to != min_letter :  # Dans le cas où le début de la séquence est déjà dans le bon ordre (Mot 2 et 3) (Cas n°2 , n°3 et n°5)
				if Spe_cond == False:  # La lettre lettre minimale n'est pas la seule bien placée (Mot 2) (Cas n°2 , n°3)
					seq_after_permutation = L[:sorted_to+i] +seq_inv + L[min_letter+1:]
				else : # Sinon la condition spéciale est vraie (Mot 3) (Cas n°5)
					first_elmt = [L[0]] # Nécessaire car sinon on traite un entier 
					seq_after_permutation = first_elmt+ seq_inv +  L[min_letter+1:]

			else :  # Si le début de la séquence n'est pas trié (Mot 1) (Cas n°4)
				if len(seq_to_permute)== len(seq_inv): # Pour la première itération
					seq_after_permutation = seq_inv +L[min_letter+1:]
				else :  # Dans les cas suivants
					seq_after_permutation = L[:len(seq_to_permute)-len(seq_inv)]+seq_inv+L[min_letter+1:]

			c_score = score(seq_after_permutation) # Calcul du nouveau score
	
			if c_score >= score_courant: # Si on a une amélioration ou une égalité 
				res.append((seq_after_permutation , c_score , dist+1 )) # On retient la permutation			
		return res

	else: # La séquence est déjà triée
		return []  # On retourne une liste vide 

def permutation_v2(L, score_courant, dist):
	"""Cettte fonction est beacoup plus simple que la première version mais également beaucoup plus itérative.
	Elle permet de générer TOUTES les permutations. Et fonctionne en particulier dans le cas du ChrIIIR.
	Attention une permutation n'est pas retenue si la distance est inférieure ou égale à len(L)-1 qui correspond en fait
	au nombre nécessaires si on réalise chaque inversion pour placer la lettre suivante dans le bon ordre.
	Je sais pas si c'est très juste mais c'est un garde fou pour éviter des calculs trop long. Je me permise
	d'écrire cette condition car si dist>len(L)-1 alors de toute façon la solution ne sera pas optimale. Cependant
	ceci modifie beaucoup la façon de calculer la distance moyenne. """

	sorted_to =  end_ord(L)
	n = len(L)
	min_letter= L.index(min(L[ sorted_to :]))
	res =[]
	if sorted_to != len(L):
		if sorted_to == min_letter :
			if min_letter ==0 :
				sorted_to +=1
			else : 
				sorted_to = 0
		for b in range(sorted_to,n-1):
			for e in range(sorted_to + 1,n):
				if  b<e :
					if dist<=len(L)-1 :
						seq_inv = inversion( L[b:e+1])
						seq_after_permutation = L[:b]+seq_inv+ L[e+1:len(L)]
						score_c = score(seq_after_permutation)
						if score_c >= score_courant :
							res.append((seq_after_permutation , score_c , dist+1 ))		

		return res
	else :
		return []

def seq_aleatoire(l_ascii): # e
	"Permet de générer une séquence alétoire de même composition que celle passée en argument"
	random.shuffle(l_ascii)
	return l_ascii


def scenario_aleatoire(l,n): # 
	"""Recherche du nombre de d'inversions minimal sur suites aléatoires

    Cette fonction prend en argument une liste d'entiers, elle la mélange
    puis calcul le nombre d'inversions minimal nécessaire la trier. Ce 
    processus est répété `n` fois. En sortie cette fonction retourne une 
    liste de taille `n` contenant le nombre d'inversions minimal trouvé 
    pour chaque test, ainsi que le nombre moyen d'inversions obtenu pour 
    une liste de taille `l`.

    Parameters
    ----------
    l : list
        `l` est une liste d'entiers.
    n : int
    	`n` nombre d'itérations à effectuer.

    Returns
    -------
    res : list
        Liste contenant le nombre minimal d'inversion obtenu pour les `n`
        répétitions.
	
    See Also
    --------
    seq_aleatoire : Genère des suites d'entiers aléatoires
    nb_inversion : Recherche itérative du nombre minimal d'inversion 

	Notes
    -----
    Étant donné que cette fonction fait appel à `nb_inversion`, elle ne peut
    être appliquée que pour des listes de petite taille, afin de garantir 
    l'éxécution du calcul dans un temps raisonnable. 
   
    Examples
    --------
	>>> L1 = [1,2,3,4,5]
	>>> scenario_aleatoire(L1,10)
	([2, 3, 3, 3, 2, 2, 3, 3, 2, 3], 2.6)

    """
	res =[]
	for i in range(n):
		L = seq_aleatoire(l)
		c_res = nb_inversion(L)
		res.append(c_res)
	moy_dist= sum(res)/len(res)
	return res, moy_dist


def scenario_aleatoire(l,runs, write, file_name=None):
	"""Scenario aleatoire prend en argument une liste d'entier correspondant au code ascii d'une séquence
	et un nombre de simulations (runs). Cette fonction calcule le nombre d'inversions nécessaires
	pour trier une séquence aléatoire et retournera une liste contenant le nombre d'inversion minimal qui 

	a été nécessaire pour résoudre chaque simulation (séquence aléatoire), ainsi que le nombre d'inversion moyen. """
	# En tête
	if write == True :
		with open(file_name, 'a') as f:
			f.write("Nb_itertion \t Min_inv \n")
		f.close()

	res =[]
	for i in range(runs):
		L = seq_aleatoire(l)
		c_res = nb_inversion(L)
		res.append(c_res)

		if write == True :
			with open(file_name, 'a') as f:
  				f.write("%d \t %d \n" %(i, c_res))
			f.close()

	moy_dist= sum(res)/len(res)
	return res, moy_dist

def stat_parente(v_alea, d_obs):
	"""Cette fonction retourne la probabilité d'observer une distance moyenne équivalente à d_obs sous l'hypothèse du hasard.
	Elle prend en argument le nombre minimal d'inversions néecessaires pour ordonner la séquence de gène (d_obs), et une liste de 
	taille |l| qui contient le nombre minimal d'inversions néecessaires pour ordonner |l| séquences aléatoires de  taille équivalente
	à la séquence d'intérêt. """
	e = 0
	for res_alea in v_alea:
		if res_alea < d_obs:
			e += 1
	prob = e/len(v_alea)
	return prob




# ---------- TESTS DES FONCTIONS ---------- #
"""		
print("\n MOT 1  ")
mot1 = "bcaed" 
L1 = ConvertAsci(mot1)
P1  = permutation(L1, score(L1), 0)
print("Adjacence L1  : ", adjacent(L1))
print("score  ", score(L1))
print("Trie jusqu a : ", end_ord(L1))
print("Permutation P1 " , P1)


print("\n MOT 2  ")
mot2 = "abedc" 
L2 = ConvertAsci(mot2)
P2  = permutation(L2, score(L2),0)
print("P2", P2)



print("\n MOT 3  ")
mot3 = "acbdfe" 
L3 = ConvertAsci(mot3)
print("Adjacence L3  : ", adjacent(L3))
print("score  ", score(L3))
P3  = permutation(L3, score(L3),0)
print("P3", P3)


print("\n MOT 3  ")
mot3 = "bcadfegih"
L3 = ConvertAsci(mot3)
print("TRie jusqua : ", end_ord(L3))
P3  = permutation(L3, score(L3),0)
print("P1", P3)
print("\n")
print('\n  Nb inversion obs   :    \n' , nb_inversion("bcadfe")  )



print("\n MOT Exemple cours   ")
mot4 = "lhfebadckijgm"
L4 = ConvertAsci(mot4)
print("Trie jusqua : ", end_ord(L4))
P4  = permutation(L4, score(L4),0)
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
P5 = permutation(L5, score(L5),0)
print("P5", P5)
print('\n')
print('\n Nb inversion obs   :    \n' , nb_inversion("ailgkjmbcefhd")  )
"""

'''
print("\n  CHROMOSOME A 6 GENES  \n")
g6 = "bcadfe"
L6 = ConvertAsci(g6)
S6 = score(L6)
d_obs6 = nb_inversion(L6 )
print('D obs', d_obs6)
print("\n Distance moyenne d'inversions calculée sur 50 scenari : d_moy=", scenario_aleatoire(L6,500, True , "6_genes.txt")[1] )
alea6 = scenario_aleatoire(L6,50, True , "6_genes.txt")[0] 
stat_aleatoire6 = stat_parente(alea6, d_obs6)
print("Stat 6 ", stat_aleatoire6 )

print("\n  CHROMOSOME A 7 GENES  \n")
g7 = "bcadfeg"
L7 = ConvertAsci(g7)
S7 = score(L7)
d_obs7 = nb_inversion(L7)
print('D obs', d_obs7)
print("\n Distance moyenne d'inversions calculée sur 50 scenari : d_moy=", scenario_aleatoire(L7,50, False )[1] )
alea7 = scenario_aleatoire(L7,500, True , "6_genes.txt")[0] 
stat_aleatoire7 = stat_parente(alea7, d_obs7)
print("Stat 6 ", stat_aleatoire7 )

print("\n  CHROMOSOME A 13 GENES  \n")
g13 = "abcdefghijklm"
L13 = ConvertAsci(g13)
S13 = score(L13)
d_obs13 = nb_inversion(L13 )
print('D obs', d_obs13)
#print("\n Distance moyenne d'inversions calculée sur 20 scenari : d_moy=",  scenario_aleatoire(L13,20, True,"13_genes.txt" )[1] )

data13 = pd.read_csv('13_genes.txt', header = None, sep='\t')
res13 = list(data13.iloc[:,1])
stat_aleatoire13 = stat_parente(res13, d_obs13)
print("Stat 13 ", stat_aleatoire7 )
'''

print("\n  VERSION 1  : \n")
print("\n  DROSOPHILES  : <3  \n")

chrIIIR= "aebcfdg"
print("Organisation du chromosome III (r) : ", chrIIIR)
LIIIR = ConvertAsci(chrIIIR)
print('SCORE CHR ,', score(LIIIR))
d_obs_IIIR = nb_inversion(LIIIR)
print('Pour le Chr III R  le nombre minimal d inversion est   : ', d_obs_IIIR)
alea_IIIR , moy_dist_IIIR= scenario_aleatoire(LIIIR,500, False)
stat_aleatoire_IIIR = stat_parente(alea_IIIR, d_obs_IIIR)
print("Distance moyenne : ", moy_dist_IIIR)
print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIIR , "(sur %s sequence aleatoires) \n"%len(alea_IIIR ))




chrIIIL= "CFEBAD"
print("Organisation du chromosome III (l) : ", chrIIIL)
LIIIL = ConvertAsci(chrIIIL)
d_obs_IIIL = nb_inversion(LIIIL)
print('Pour le Chr III R  le nombre minimal d inversion est   : ', d_obs_IIIL)
alea_IIIL , moy_dist_IIIL= scenario_aleatoire(LIIIL,500, False)
stat_aleatoire_IIIL = stat_parente(alea_IIIL, d_obs_IIIL)
print("Distance moyenne : ", moy_dist_IIIL)
print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIIL , "(sur %s sequence aleatoires) \n"%len(alea_IIIL ))


chrIIR= "ACEBFD"
print("Organisation du chromosome II (r) : ", chrIIR)
LIIR = ConvertAsci(chrIIR)
d_obs_IIR = nb_inversion(LIIR)
print('Pour le Chr III R  le nombre minimal d inversion est   : ', d_obs_IIR)
alea_IIR , moy_dist_IIR= scenario_aleatoire(LIIR,500, False)
stat_aleatoire_IIR = stat_parente(alea_IIR, d_obs_IIR)
print("Distance moyenne : ", moy_dist_IIR)
print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIR , "(sur %s sequence aleatoires) \n"%len(alea_IIR ))


chrIIL= "DEFACB"
print("Organisation du chromosome II (l) : ", chrIIL)
LIIL = ConvertAsci(chrIIL)
d_obs_IIL = nb_inversion(LIIL)
print('Pour le Chr III R  le nombre minimal d inversion est   : ', d_obs_IIL)
alea_IIL, moy_dist_IIL = scenario_aleatoire(LIIL,500, False)
print("Distance moyenne : ", moy_dist_IIL)
stat_aleatoire_IIL = stat_parente(alea_IIL, d_obs_IIL)
print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIL , "(sur %s sequence aleatoires) \n"%len(alea_IIL ))


chrX= "LHFEBADCKIJGM"
print("Organisation du chromosome X : ", chrX)
LX = ConvertAsci(chrX)
d_obs_X = nb_inversion(LX)
print('Pour le Chr III R  le nombre minimal d inversion est   : ', d_obs_X)
#alea_X = scenario_aleatoire(LX,500, False)[0] 
data13 = pd.read_csv('13_genes.txt', header = None, sep='\t')
res13 = list(data13.iloc[:,1])
moy_dist_X = sum(res13)/len(res13)
stat_aleatoire_X = stat_parente(res13, d_obs_X)
print("Distance moyenne : ", moy_dist_X)
print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_X , "(sur %s sequence aleatoires) \n"%len(res13 ))






print("\n  VERSION 2  : \n")
print("\n  DROSOPHILES  : <3  \n")

chrIIIR= "aebcfdg"
print("Organisation du chromosome III (r) : ", chrIIIR)
LIIIR = ConvertAsci(chrIIIR)
print('SCORE CHR ,', score(LIIIR))
d_obs_IIIR = nb_inversione(LIIIR)
print('Pour le Chr III R  le nombre minimal d inversion est   : ', d_obs_IIIR)
#alea_IIIR = scenario_aleatoire(LIIIR,500, False)[0] 
#stat_aleatoire_IIIR = stat_parente(alea_IIIR, d_obs_IIIR)
#print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIIR , "(sur %s sequence aleatoires) \n"%len(alea_IIIR ))


chrIIIL= "CFEBAD"
print("Organisation du chromosome III (l) : ", chrIIIL)
LIIIL = ConvertAsci(chrIIIL)
d_obs_IIIL = nb_inversion(LIIIL, True)
print('Pour le Chr III RL le nombre minimal d inversion est   : ', d_obs_IIIL)
#alea_IIIL = scenario_aleatoire(LIIIL,500, False)[0] 
#stat_aleatoire_IIIL = stat_parente(alea_IIIL, d_obs_IIIL)
#print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIIL , "(sur %s sequence aleatoires) \n"%len(alea_IIIL ))


chrIIR= "ACEBFD"
print("Organisation du chromosome II (r) : ", chrIIR)
LIIR = ConvertAsci(chrIIR)
d_obs_IIR = nb_inversion(LIIR, True)
print('Pour le Chr II R  le nombre minimal d inversion est   : ', d_obs_IIR)
#alea_IIR = scenario_aleatoire(LIIR,500, False)[0] 
#stat_aleatoire_IIR = stat_parente(alea_IIR, d_obs_IIR)
#print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIR , "(sur %s sequence aleatoires) \n"%len(alea_IIR ))


chrIIL= "DEFACB"
print("Organisation du chromosome II (l) : ", chrIIL)
LIIL = ConvertAsci(chrIIL)
d_obs_IIL = nb_inversion(LIIL, True)
print('Pour le Chr II L  le nombre minimal d inversion est   : ', d_obs_IIL)
#alea_IIL = scenario_aleatoire(LIIL,500, False)[0] 
#stat_aleatoire_IIL = stat_parente(alea_IIL, d_obs_IIL)
#print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_IIL , "(sur %s sequence aleatoires) \n"%len(alea_IIL ))

chrX= "LHFEBADCKIJGM"
print("Organisation du chromosome X : ", chrX)
LX = ConvertAsci(chrX)
d_obs_X = nb_inversion(LX, True)
print('Pour le Chr X  le nombre minimal d inversion est  : ', d_obs_X)
#alea_X = scenario_aleatoire(LX,500, False)[0] 
data13 = pd.read_csv('13_genes.txt', header = None, sep='\t')
res13 = list(data13.iloc[:,1])
print(sum(res13)/len(res13))
#stat_aleatoire_X = stat_parente(res13, d_obs_X)
#print("Probabilite qu'une telle distance soit due au hasard :  ", stat_aleatoire_X , "(sur %s sequence aleatoires) \n"%len(res13 ))



