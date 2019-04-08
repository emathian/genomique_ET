data <- read.csv("8F0EB0CW11N-Alignment-HitTable.csv", header=FALSE)
q.start <- data$V7
q.end <- data$V8
s.start <- data$V9
s.end <- data$V10

###########################################################################################

# REMETRE LES COLONNES END ET START DANS L'ORDRE
data_ordre=data
n=length(q.start)
for(i in 1:n){
  # test des sens de lecture
  if(s.start[i]>s.end[i]){
    # s.start est la fin et s.end est le debut
    # on les echange
    data_ordre$V9[i]=s.end[i] #v9=s.start, v10=s.end
    data_ordre$V10[i]=s.start[i]
  }
  if(q.start[i]>q.end[i]){
    # q.start est la fin et q.end est le debut
    # on les echange
    data_ordre$V7[i]=q.end[i] #v7=q.start, v8=q.end
    data_ordre$V8[i]=q.start[i]
  }
}
s.start=data_ordre$V9
s.end=data_ordre$V10
q.start=data_ordre$V7
q.end=data_ordre$V8

###############################################################################################

# DOT MATRIX (SANS LES SEGMENTS FUSIONES)
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000))
segments(q.start, s.start, q.end, s.end)


################################################################################################

# FILTRER LA DOT MATRIX (SANS LES SEGMENTS FUSIONES)
data_filtre=data_ordre[FALSE,]
n=length(q.start)
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000))
for(i in 1:n){
  # valeur seuil arbitraire...
  if(abs(q.start[i]-q.end[i])>2500 || abs(s.start[i]-s.end[i])>2500){
    segments(q.start[i], s.start[i], q.end[i], s.end[i]) 
    data_filtre <- rbind.data.frame(data_filtre, as.data.frame(data_ordre[i,]))
  }
}

s.start=data_filtre$V9
s.end=data_filtre$V10
q.start=data_filtre$V7
q.end=data_filtre$V8


##############################################################################################    

# FUSIONER LES SEGMENTS TRES PROCHES (APRES AVOIR REMIS LES COL. START ET END DANS L'ORDRE)
data_fusion=data_filtre
n=length(q.start)
for(i in 1:n){
  for(j in 1:n){
<<<<<<< HEAD
    if(q.start[j]>q.start[i]){
      if(abs(s.start[j]-s.end[i]) < 533 & q.start[j]-q.end[i] < 3000){ # seuil arbitraire inferieur au 1er quartile de abs(s.start-s.end)
       #if(abs(s.start[j]-s.end[i]) < 533){
        # alors on fusionne les fragments i et j (qui deviennent un unique fragment i)
        data_fusion$V8[i]=data_fusion$V8[j] # q.end
        data_fusion$V10[i]=data_fusion$V10[j] #s.end
        data_fusion$V7[j]="FALSE" # q.start >> emp??che la ligne j d'??tre consid??r??e dans les boucles suivantes 
      }
=======
    if(i!=j & data_fusion$V7[j]!="FALSE"){
      #if(q.start[j]>q.start[i]){
        #if(abs(s.start[j]-s.end[i]) < 1000 & q.start[j]-q.end[i] < 1000){ # seuil arbitraire inferieur au 1er quartile de abs(s.start-s.end)
        if((abs(s.start[j]-s.end[i]) < 1000 & abs(q.start[j]-q.end[i]) < 1500) || (abs(s.start[j]-s.end[i]) < 1500 & abs(q.start[j]-q.end[i]) < 1000)){ # seuil arbitraire inferieur au 1er quartile de abs(s.start-s.end)
          # alors on fusionne les fragments i et j (qui deviennent un unique fragment i)
          data_fusion$V8[i]=data_fusion$V8[j] # q.end
          data_fusion$V10[i]=data_fusion$V10[j] #s.end
          data_fusion$V7[j]="FALSE" # q.start >> empêche la ligne j d'être considérée dans les boucles suivantes 
        }
      #}
>>>>>>> 5996becbbb3cc8e9e8033842478c439b7aca9d3e
    }
  }  
}

##################################################################################################

# SUPPRESSION DES LIGNES AVEC DES FALSE 
data_fusion=data_fusion[!grepl("FALSE", data_fusion$V7),]

q.start_f <- as.numeric(data_fusion$V7)
q.end_f <- as.numeric(data_fusion$V8)
s.start_f <- data_fusion$V9
s.end_f <- data_fusion$V10

###################################################################################################

# DOT MATRIX AVEC LES SEGMENTS FUSIONES
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000))
segments(q.start_f, s.start_f, q.end_f, s.end_f)

######################################################################################################

# FILTRAGE FINAL DE LA DOT MATRIX
data_filtre_fin=data_fusion[FALSE,]
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000))
n=length(q.start_f)
for(i in 1:n){
  # valeur seuil arbitraire...
  if(abs(q.start_f[i]-q.end_f[i])>50000 || abs(s.start_f[i]-s.end_f[i])>50000){
    segments(q.start_f[i], s.start_f[i], q.end_f[i], s.end_f[i])
    data_filtre_fin <- rbind.data.frame(data_filtre_fin, as.data.frame(data_fusion[i,]))
  }
}

<<<<<<< HEAD

data <- data.frame(ID = seq(1:length(q.start_f)),Qstart = q.start_f , Qend = q.end_f , Sstart = s.start_f , Send = s.end_f)
write.table(data, file = "data.txt", quote = FALSE, sep = "\t", col.names = TRUE)
=======
q.start_f2 <- as.numeric(data_filtre_fin$V7)
q.end_f2 <- as.numeric(data_filtre_fin$V8)
s.start_f2 <- data_filtre_fin$V9
s.end_f2 <- data_filtre_fin$V10

######################################################################################################

# COMPARAISON TAUX DE SIMILARITE

s.start=data_ordre$V9
s.end=data_ordre$V10
q.start=data_ordre$V7
q.end=data_ordre$V8

# CHEZ LES ALIGNEMENTS GARDES
long_segments_f2 = sqrt((q.end_f2- q.start_f2)^2 + (s.end_f2- s.start_f2)^2 ) # longeur des segments de la dot_matrix
simi_garde = sum(long_segments_f2)/length(q.start_f2) # on divise par le nombre de segments
taux_garde = simi_garde/max(s.end) # on divise par la taille du génome s

# CHEZ LA TOTALITE DES ALIGNEMENTS 
long_segments_tot = sqrt((q.end- q.start)^2 + (s.end- s.start)^2 ) # longeur des segments de la dot_matrix
simi_tot = sum(long_segments_tot)/length(q.start) # on divise par le nombre de segments
taux_tot = simi_tot/max(s.end) # on divise par la taille du génome s
>>>>>>> 5996becbbb3cc8e9e8033842478c439b7aca9d3e
