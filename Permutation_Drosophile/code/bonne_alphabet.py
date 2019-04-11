# -*- coding: utf-8 -*-
""" Ce programme a été rédigé pour la recherche du nombre minimal d'inversion à réaliser pour 
ordonner une séquence, attention c'est un problème NP complet. Nous avons donc implémenter une heuristique,
celle-ci est donc utilisable sur de petites séquences. Ce programme répond à des questions d'organisation des
chromosomes, dans le but de recherche de liens de parenté."""


from __future__ import division
import random
import copy as cp
import pandas as pd

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


def ConvertAsci(L):
    """Converti les éléments d'une liste de lettres en entiers.
    
    Cette fonction converti une liste de caractères en une liste d'entier correspondant à leur code ascii.

    Parameters
    ----------
    L : list
        `L` est une liste de caractères.

    Returns
    -------
    La : list
        `La` est une liste d'entiers correspondant aux codes ascii de la liste `L`.

    Examples
    --------
    >>> L = ["a","b","c","e","j"]
    >>> ConvertAsci(L)
    [97, 98, 99, 101, 106]

    """
    assert(type(L[0])== str)
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
        `adj` est une liste de listes contenant tous les couples d'indice
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
    assert(type(L[0])== int)
    adj=[] 
    for i in range(len(L)-1):
        if L[i]==L[i+1]+1 : 
            adj.append([i, i+1])
        elif L[i]==L[i+1]-1:
            adj.append([i,i+1])
    return adj


def score(L):
    """Calcul un score d'ordonnancement d'une liste d'entiers.

    Cette fonction calcul le nombre de couples de lettres qui sont consécutives
    dans l'ordre alphabétique et vérifie également si le min(L) est en position 0
    et si le max(L) est en position -1. `L` est une liste de caractères convertis en
    code ascii.
    
    Parameters
    ----------
    L : list 
        `L` est une liste d'entiers.

    Returns
    -------
    score : int
        `score` est un etier proportionnel à l'ordonnancement de la liste `L`.

    See Also
    --------
    adjacent : Recherche de l'ensemble des éléments consécutifs d'une liste d'entiers.

    Examples
    --------
    >>> L1 = [97,98,99,101,106]
    >>> score(L1)
    4
    >>> L3 = [2,4,1,3]
    >>> score(L3)
    0
    
    """
    assert(type(L[0])== int)
    score=len(adjacent(L))
    if L.index(min(L))==0:
        score+=1
    if L.index(max(L))==len(L)-1:
        score+=1
    return score


def end_ord(l) :
    """Recherche l'indice du premier élément non trié.

    Cette fonction recherche le premier élément d'une liste d'entiers
    qui n'est pas dans l'ordre numérique croissant et retourne son indice. Si la
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
        `int` est l'indice du premier élément mal positionné de `l`.

    See Also
    --------
    permutation : Recherche itérative de toutes les inversions permettant d'améliorer le score.
    nb_inversion : Recherche itérative du nombre minimal d'inversion.

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
    assert(type(l[0])== int)
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


def nb_inversion(l, v2 = False):
    """Calcul le nombre d'inversion nécéssaire dans une chaine de caractères composées de lettre de l'alphabet consécutives pour atteindre l'ordre alphabétique.

    Cette fonction calcul le nombre minimum d'inversions necessaires pour obtenir une chaine de caractère odonnée dans une chaine 
    de caractères composées de lettre de l'alphabet consécutives. L'utilisateur peut choisir d'appeler une version v2
    de la fonction permutation dans le cas où la chaine de caractère est courte ou si il lance la fonction scenario_aleatoire. 
    Par défaut v2=False, pour utiliser v2 donner en paramètre v2=True.

    Parameters
    ----------
    l : list
        `l` est une chaîne de caractères.
    v2 : bool
        `v2` est un booleen qui vaut False par défaut et entraine l'utilisation de la fonction permutation. 
        Si l'utilisateur donne en argument v2=True alors c'est la fonction permutation_v2 qui est appelée.

    Returns
    -------
    min_nb_inv : int
        `min_nb_inv` est un entier représentif du nombre d'inversion minimum dans une liste pour atteindre l'ordre alphabétique.

    See Also
    --------
    ConvertAsci : Converti les elements d'une liste en l_ascii.
    score : Calcul un score de ressamblance à l'ordre alphabétique pour une liste de code ascii.
    permutation : Recherche itérative de toutes les inversions permettant d'améliorer le score.
    permutation_v2 : Recherche exhaustive des inversions.

    Examples
    --------
    >>> l1 = "abcdef"
    >>> nb_inversion(l1)
    0
    >>> l2 = "cdab"
    >>> nb_inversion(l2)
    2
    >>> l3 = "aebcfdg"
    >>> nb_inversion(l3,v2=False)
    4
    >>> nb_inversion(l3)
    4
    >>> nb_inversion(l2,v2=True)
    2
    >>> nb_inversion(l2,True)
    2
    
    """
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
    """Recherche presque exhaustive des inversions dans une liste d'entiers pour l'ordonner.

    Cette fonction prend en argument une liste d'entiers, son `score_courant`
    (cf : `score`), ainsi que sa distance à l'origine (i.e. à la séquence initiale).
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
        Score de la liste (cf : `score`).
    dist :  int
        `dist` est la distance à l'origine pour la séquence `L`, traduit le nombre d'inversions
        qui ont déjà été réalisées sur `L`.

    Returns
    -------
    res : liste de tuples
        `res` est une liste contanant autant de tuple que d'inversions
        conservées. Chaque tuple est constitué de la séquence après
        inversion, de son score et de sa distance (`dist` + 1).

    See Also
    --------
    nb_inversion   : Recherche itérative du nombre minimal d'inversion.
    permutation_v2 : Recherche exhaustive des inversions.

    Notes
    -----
    Étant donné que cette fonction fait appel à `nb_inversion`, elle ne peut
    être appliquée que pour des listes de petite taille, afin de garantir
    l'éxécution du calcul dans un temps raisonnable.

    `permutation` gère les cas suivants :
    1 : Si `L` est déjà triée alors une liste vide est renvoyée.

    2 : Si et seulement si le début de `L` est trié la séquence à
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
    
    Attention cette fonction ne permet pas d'obtenir le nombre 
    minimal d'inversion dans le cas où la séquence à inverser
    n'est pas contenure entre la séquence déjà triée et la lettre
    minimal.

    Exemple:
    Mot = A E B C F D G
    1   : A B E C F D G
    2   : A B C E F D G
    3   : A B C D F E G
    4   : A B C D E F G

    Dans ce cas très précis le nombre d'inversion minimal est 
    trois ainsi la version 2 de permutation doit être utilisée.

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
    assert(type(L[0])== int)
    assert(type(score_courant)==int)
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
    """Recherche exhaustive des inversions pour l'ordonner.

    Cette fonction prend en argument une liste d'entiers, son `score_courant`
    (cf : `score`), ainsi que sa distance à l'origine (à la séquence initiale).
    En effet elle est appellée par la procédure `nb_inversion`, qui détermine
    le nombre d'inversions nécessaires pour trier une liste, ce nombre
    d'inversions détermine la distance l'origine d'une possibilité. 
    Cette fonction est donc semblable à `permutation`. Cette version permet 
    toutefois une recherche exhaustive de toutes les permutations. Le nombre 
    de combinaison pouvant être relativement grand, cette fonction n'est adaptée
    que pour des séquences de taille inférieurs 8. 

    Ainsi étant donné une liste et son état courant, `permutation_v2` recherhe
    la partie de la séquence qui  a déjà été ordonnée, puis génère toute les 
    inversion possible. Une inversion sera retenue si et seulement si elle permet
    de conserver ou d'augmenter le score.

    La fonction `permutation_v2` retourne ainsi la liste de toute les inversions. 
    À chaque élément de la liste des résultats est associé la séquence d'entiers,
    le score associé à cette séquence et la distance à l'origine. En effet la 
    distance de chaque séquences retenue est incrémentée d'une unité, étant 
    donné qu'elles sont la résultante d'une inversion.

    Parameters
    ----------
    L : list
        `L` est une liste d'entiers.
    score_courant : int
        Score de la liste (cf : `score`).
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
    nb_inversion   : Recherche itérative du nombre minimal d'inversion
    permutation    : Recherche exhaustive des inversions

    Notes
    -----
    Étant donné que cette fonction fait appel à `nb_inversion`, elle ne peut
    être appliquée que pour des listes de petite taille, afin de garantir
    l'éxécution du calcul dans un temps raisonnable. Ceci est particulièrement
    pour cette deuxième version de `permutation_v2`.

    Etant donné une séquence `L` `permutation_v2`, recherche la partie déjà 
    triée, de taille N. Pour la séquence à trier elle génere toutes les permutation
    possibles. Pour ce faire elle commence donc à itérer à partir de la première 
    lettre non triée d'indice N+1 , et génère toutes les permutations pour cette 
    position. Puis elle recommence pour la deuxième lettre non triée etc...
    Les inversions testées peuvent être résumées  telles que :
    .. math::
    
        perm(i,N+j) = \\sum_{i=1}^{i=L-(N+j-1)} inv(L[N+j : N+j+i])

    Dans cette formule i correspond à la i ème permutation, et N+j
    à la position de lettre non triée considérée. À chaque itération les éléments
    d'indice compris entre (N+j) et  et (N+j+i) sont inversés
    

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


def seq_aleatoire(l_ascii):
    """Mélange une liste.

    Cette fonction permet de générer une séquence alétoire de même
    composition que celle passée en argument.

    Parameters
    ----------
    l_ascii : list
        `l_ascii` est une liste d'entiers.

    Returns
    -------
    l_ascii : list
        `l_ascii` est une liste d'entiers qui correspond à la liste donnée en argument ordonnée différemment.

    """
    random.shuffle(l_ascii)
    return l_ascii


def scenario_aleatoire(l,n, write, file_name=None):
    """Recherche du nombre d'inversions minimal dans une liste aléatoires d'entiers consecutifs.

    Cette fonction prend en argument une liste d'entiers, elle la mélange
    puis calcul le nombre d'inversions minimal nécessaire la trier. Ce
    processus est répété `n` fois. En sortie cette fonction retourne une
    liste de taille `n` contenant le nombre d'inversions minimal trouvé
    pour chaque test, ainsi que le nombre moyen d'inversions obtenu pour
    une liste de taille `l`. L'utilisateur peut choisir d'enregistrer les
    résultats dans un fichier texte pour cela il doit préciser le non du 
    fichier. 

    Parameters
    ----------
    l : list
        `l` est une liste d'entiers.
    n : int
        `n` nombre d'itérations à effectuer.
    write : bool
        `write` est un booléen si la fonction écrit ou non les résultats dans un fichier.
    file_name : 
        `file_name` est le nom du fichier qui contiendra les résultat si write = True.
    Returns
    -------
    res : list
        `res` est une liste contenant le nombre minimal d'inversion obtenu pour les `n`
        répétitions.

    See Also
    --------
    seq_aleatoire : Genère des suites d'entiers aléatoires.
    nb_inversion : Recherche itérative du nombre minimal d'inversion.

    Notes
    -----
    Étant donné que cette fonction fait appel à `nb_inversion`, elle ne peut
    être appliquée que pour des listes de petite taille, afin de garantir
    l'éxécution du calcul dans un temps raisonnable.

    """
    if write == True :
        with open(file_name, 'a') as f:
            f.write("Nb_itertion \t Min_inv \n")
        f.close()

    res =[]
    for i in range(n):
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
    """Calcul la probabilité d'observer une distance moyenne équivalente à `d_obs` sous l'hypothèse du hasard.

    Cette fonction retourne la probabilité d'observer une distance moyenne équivalente à `d_obs` sous l'hypothèse du hasard.
    Elle prend en argument le nombre minimal d'inversions néecessaires pour ordonner la séquence de gène (`d_obs`), et une liste de
    taille `l` qui contient le nombre minimal d'inversions néecessaires pour ordonner `l` séquences aléatoires de taille équivalente
    à la séquence d'intérêt. 

    Parameters
    ----------
    v_alea : list
        `v_alea` est une liste d'entiers.
    d_obs : int
        `d_obs` nombre minimal d'inversions néecessaires pour ordonner la séquence de gène.

    Returns
    -------
    prob : list
        `prob` est une liste contenant le nombre minimal d'inversion obtenu pour les `n`
        répétitions.

    Notes
    -----
    La statistique retournée correspond à une proportion telle que :

    .. math::
    
        P     =  \\frac{X}{N} 
       

    Où X est le nombre d'inversions aléatoires inférieures à l'observation, et N le nombre total de simulations éffectuées qui
    correspond à la taille de `v_alea`

    Examples
    --------
    >>> v = [1,2,3,4,5]
    >>> d = 4
    >>> stat_parente(v,d)
    0.6
    
    """
    e = 0
    for res_alea in v_alea:
        if res_alea < d_obs:
            e += 1
    prob = e/len(v_alea)
    return prob





if __name__ == '__main__':    

    import doctest
    doctest.testmod()
