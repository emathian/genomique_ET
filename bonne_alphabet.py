import random
import copy as cp


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy as cp

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

##def MinInvers(L):
#    """ trouve le nombre min d'inversions nécessaires pour mettre la liste de caractères L dans l'ordre alphabétique"""
#    ### trouver l'indice de la plus petite lettre



def end_ord(l) :
	"""prend en argument une liste de codes ASCII et renvoie l'indice de la première lettre qui n'est plus dans l'ordre alphabetique"""
	ind=0
	while l[ind+1]==l[ind]+1:
		ind+=1
	return ind+1

#print(end_ord(L1))

def main(l):
	""" prend en argument une liste de chaine de caractères composées de lettre de l'alphabet retourne le nobre minimum d'inversions necessaires pour obtenir une liste dans m'ordre alphabetique"""
	nb_inv=0#initialisation du nombre d'inversion
	l_ascii=ConvertAsci(l) #converti en liste de code ascii
	s=Score(l_ascii)#score initial de la sequence
	



def permutation(liste_ascii, current_score):
	"""permutation takes as input a liste of ascii and the current  score. It returns list of tuple, each element contains
	the list of ascii and the score linked to this permutation """
	sorted_to =  end_ord(liste_ascii) # Retourne l'indice de la lettre qui n'est plus dans l'ordre
	#print("BEFORE" , "liste ascii "  , liste_ascii , "current score " , current_score )
	#print(" liste ascii ever sorted  "  , liste_ascii[ : sorted_to])
	min_letter= liste_ascii.index(min(liste_ascii[ sorted_to :]))
	#print(" min letter  "  , min_letter)
	seq_to_permute =liste_ascii[ sorted_to :min_letter + 1]  
	#print(" seq _ to permute  "  , seq_to_permute)
	score_before_permut = Score(liste_ascii)
	seq_after_permutation =[]
	res = []
	for i in range(len(seq_to_permute)):
		seq_inv = Inversion(seq_to_permute[i:])
		#print("seq_inv" , seq_inv )
		seq_after_permutation = liste_ascii[:sorted_to] +seq_inv +liste_ascii[min_letter+1:]
		#print ("seq_after_permutation" , seq_after_permutation)
		c_score = Score(seq_after_permutation)
		#print("c_score" , c_score , "current score" , current_score)
		if c_score > current_score:
			
			res.append((seq_after_permutation , c_score ))
		print("res" , res) 
	return res
			



L=["a","c","d","b"]
L1=[1,2,3,5,4]
mot1 = "abcd" 
print(Inversion(mot1))
print(ord('A'))
print(chr(65))                                                                                                                                           

mot2 = "abcdlhfekijgm"
to_ascii_2 = ConvertAsci(mot2)
Score2 = Score(to_ascii_2)
print(permutation(to_ascii_2 , Score2))

