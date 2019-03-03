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


def main(l):


	""" prend en argument une liste de chaine de caractères composées de lettre de l'alphabet retourne le nobre minimum d'inversions necessaires pour obtenir une liste dans m'ordre alphabetique"""
	#initialisation du nombre d'inversion
	print("MOT   : " , l )
	l_ascii= ConvertAsci(l) #converti en liste de code ascii
	print("ConvertAsci", l_ascii)
	s=Score(l_ascii)#score initial de la sequence
	print("Score 1  :  ", s)
	l_nb_inv = []

	P  = permutation(l_ascii , s ) # Stack
	print("Vecteur de permutation BEFORE the while ", P)
	nb_inv = 0
	while len(P) != 0 : # Tant que la pile n'est pas vide 
		nb_inv += 1
		l_ascii = P[0][0]
		s = P[0][1]
		print ('Score ' , s)
		print ('l ascii after permutation ' , l_ascii)
		print ('NB INVERSION  ' , nb_inv)
		if s!= len(l_ascii)+1  : # Si la seqence n'est pas trier
			p = permutation(l_ascii , s)
			P.pop() # Retire la permutation en cours de traitement 
			P = P + p # Commande préférable à append pour éviter l'obtention de liste de liste 
			print("Vecteur de permutation ", P)
		else :
			P.pop()
			l_nb_inv.append(nb_inv)
			print('l_nb_inv' , l_nb_inv)
			nb_inv = 0
	return l_nb_inv


	# """ prend en argument une liste de chaine de caractères composées de lettre de l'alphabet retourne le nobre minimum d'inversions necessaires pour obtenir une liste dans m'ordre alphabetique"""
	# #initialisation du nombre d'inversion
	# print("MOT   : " , l )
	# l_ascii= ConvertAsci(l) #converti en liste de code ascii
	# print("ConvertAsci", l_ascii)
	# s=Score(l_ascii)#score initial de la sequence
	# print("Score 1  :  ", s)
	# l_nb_inv = []
	# if s!= len(l_ascii) +1 :
	# 	P  = permutation(l_ascii , s ) # Stack
	# 	print("Vecteur de permutation BEFORE the while ", P)
	# 	nb_inv = 1 
	# 	l_nb_inv.append(nb_inv)
	# while len(P) != 0 : # Tant que la pile n'est pas vide 
	# 	if s!= len(l_ascii)+1  : # Si la seqence n'est pas trier
	# 		l_ascii = P[0][0]
	# 		print ('l ascii after permutation ' , l_ascii)
	# 		s = P[0][1]
	# 		print ('Score ' , s)
	# 		p = permutation(l_ascii , s)
	# 		P.pop() # Retire la permutation en cours de traitement 
	# 		P = P + p # Commande préférable à append pour éviter l'obtention de liste de liste 
	# 		print("Vecteur de permutation ", P)
	# 		nb_inv +=1 
	# 	else :
	# 		l_nb_inv.append(nb_inv)

	# return l_nb_inv

	# # while s != len(l_ascii)+1: # Si la série n'est pas délà triée 
	# 	P = permutation(l_ascii, s) 
	# 	print('P', P )
	# 	nb_inv +=1 # Une inversion a été nécessaire
	# 	for ele in P :
	# 		l_ascii = ele[0]
	# 		s = ele[1]  
	# 		while s != len(l_ascii)+1: # Tant que la série n'est pas triée
	# 			P = permutation(l_ascii, s)
	# 			print("P", P)
	# 			l_ascii = P[0][0]
	# 			s = P[0][1]
	# 			nb_inv 	+=1
	# 			print("NB INV" , nb_inv )
	# 	l_nb_inv.append(nb_inv)		
	# return l_nb_inv
	

def permutation(liste_ascii, current_score):
	"""permutation takes as input a liste of ascii and the current  score. It returns list of tuple, each element contains
	the list of ascii and the score linked to this permutation """
	print('liste ascii berfore permutaton   : ' , liste_ascii)
	sorted_to =  end_ord(liste_ascii) # Retourne l'indice de la lettre qui n'est plus dans l'ordre
	
	if sorted_to != len(liste_ascii):
		print("sorted_to    :   ", sorted_to)
		min_letter= liste_ascii.index(min(liste_ascii[ sorted_to :]))
		print("min letter   :   ", min_letter)
		if sorted_to != min_letter :
			seq_to_permute =liste_ascii[ sorted_to :min_letter + 1]  
		else : # Permutation du premier element
			seq_to_permute =liste_ascii[ : sorted_to  + 1]  
		print("seq_to_permute", seq_to_permute)
		seq_after_permutation =[]
		print("current_score " , current_score)
		res = []
		for i in range(len(seq_to_permute)-1):
			print('iteration i', i)
			seq_inv = Inversion(seq_to_permute[i:])
			print("seq_inv", seq_inv)
			if sorted_to != min_letter :
				seq_after_permutation = liste_ascii[:sorted_to+i] +seq_inv +liste_ascii[min_letter+1:]
				print("seq_after_permutation" , seq_after_permutation)
			else :
				if len(seq_to_permute)== len(seq_inv):
					seq_after_permutation = seq_inv +liste_ascii[min_letter+1:]
					print("seq_after_permutation" , seq_after_permutation)
				else :
					seq_after_permutation = liste_ascii[:len(seq_to_permute)-len(seq_inv)]+seq_inv+liste_ascii[min_letter+1:]
					print("seq_after_permutation" , seq_after_permutation)
			c_score = Score(seq_after_permutation)
			print("c_score" , c_score)
			if c_score > current_score:
				print(" c_score > current_score  => T")
				res.append((seq_after_permutation , c_score ))			
		return res
	else: 
		print('The sequence is ever sorted')
		return []	
			




print("\n MOT 1  ")
mot1 = "bcaed" 
# print(Inversion(mot1))
L1 = ConvertAsci(mot1)
# print("Dernière en ordre" , end_ord(L1))
P1  = permutation(L1, Score(L1))
print("Permutation P1 " , P1)


print("\n MOT 2  ")
mot1 = "abedc" 
# print(Inversion(mot1))
L1 = ConvertAsci(mot1)
# print("Dernière en ordre" , end_ord(L1))
print("Adjacence L1  : ", Adjacent(L1))
print("Score  ", Score(L1))
print("TRie jusqua : ", end_ord(L1))
P1  = permutation(L1, Score(L1))
print("P1", P1)
# mot2 = "abcdlhfekijgm"
# l2 = ConvertAsci(mot2)
# print("mot 2" , mot2)
# print(permutation(l2, Score(l2)))
# P2 = permutation(l2, Score(l2))
# print("P2   ", P2)
# #print("\n MAIN \n ",  main(l2,0))
# mot3 = "abedc"
# l3 = ConvertAsci(mot3)
# print("\n MOt 3 SCORE   : ", Score(l3)) 
# print("\n  PERMUTATION DE MOT 3 :" , permutation(l3, Score(l3)))
# P3  = permutation(l3, Score(l3))
# print("P3   ", P3)
# print(P2)
# P2 = P2  + P3
# #P2.append(P1)
# print("PP		: "   , P2 ,
# 	"\n  PP[0]" , P2[0] ,
# 	"\n  PP[1]" , P2[1])

print("\n MOT 3  ")
mot3 = "bcadfe"
L3 = ConvertAsci(mot3)
print("TRie jusqua : ", end_ord(L3))
P3  = permutation(L3, Score(L3))
print("P1", P3)

print("\n")
#print('\n MAin    :    \n' , main("baedc")  )
print('\n MAin    :    \n' , main("bcadfe")  )
#to_ascii_2 = ConvertAsci(mot2)
#Score2 = Score(to_ascii_2)

#print("\n \n  MAIN  : " , main(mot2))
