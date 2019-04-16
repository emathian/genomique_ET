
# Introduction 

Ce programme a été écrit sous R, il est contenu dans le fichier `dot_matrix_vf.R`.  Il permet de construire la matrice des positions des gènes orthologues, partagés par la souche médiévale de la peste noire et la souche actulle de Yernisia pestis CO92. 

# Dot matrix initiale

Nous avons aligné les deux séquences sur BLAST et nous avons ainsi pu reproduire sur R la dot matrix correspondante :

![Dot matrix initiale](dot_matrix_non_filtree.png)

# Dot matrix finale

Après plusieurs étapes de filtrage et de fusion des segments orthologues, nous conservons 21 fragments et nous avons ainsi obtenu la dot matrix suivante :

![Dot matrix finale](dot_matrix_filtree_vf.png)

# Caractérisation du génome de Yernisia pestis CO92 et de la souche médiévale

Une caractérisation des génomes étudiés a été réalisée grâce au programme `comptage.py`, à partir des données génomiques `1348_chromosome.txt` et `Yernisia_pestis.txt`.
