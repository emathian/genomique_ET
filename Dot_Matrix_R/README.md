
# Introduction 

Ce programme a été écrit sous R, il permet de construire la matrice des positions des gènes orthologues, entre la souche médiévale de la peste noire et la souche actulle de  Yersinia pestis CO92. 

# Dot matrix initiale

Le génome actuel possède 3551058 bases et elles sont toutes définies alors que le génome médiéval possède 3533579 bases dont 25769 ne sont pas définies. Le génome actuel est donc plus grand que le génome médiéval.
Nous avons aligné les deux séquences sur BLAST et nous avons ainsi pu reproduire sur R la dot matrix correspondante :

![Dot matrix initiale](Initial_dot_matrix.png)

# Dot matrix finale

Après plusieurs étapes de filtrage et de fusion des segments orthologues, nous conservons 21 fragments et nous avons ainsi obtenu la dot matrix suivante :

![Dot matrix finale](dot_matrix_v3.png)