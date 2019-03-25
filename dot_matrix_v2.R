data <- read.table("pestis_1348_co92_Alignment_hit_table.txt")
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
plot(q.start[2], s.start[2], cex=.1, pch=1)
segments(q.start, s.start, q.end, s.end)

##############################################################################################    

# FUSIONER LES SEGMENTS TRES PROCHES (APRES AVOIR REMIS LES COL. START ET END DANS L'ORDRE)
data_fusion=data_ordre
n=length(q.start)
for(i in 1:n){
  for(j in 1:n){
    if(q.start[j]>q.start[i]){
      if(abs(s.start[j]-s.end[i]) < 100 & q.start[j]-q.end[i] < 1000){ # seuil arbitraire inferieur au 1er quartile de abs(s.start-s.end)
        # alors on fusionne les fragments i et j (qui deviennent un unique fragment i)
        data_fusion$V8[i]=data_fusion$V8[j] # q.end
        data_fusion$V10[i]=data_fusion$V10[j] #s.end
        data_fusion$V7[j]="FALSE" # q.start >> empêche la ligne j d'être considérée dans les boucles suivantes 
      }
    }
  }
}

##################################################################################################

# SUPPRESSION DES LIGNES AVEC DES FALSE 
data_fusion=data_fusion[!grepl("FALSE", data_fusion$V7),]

q.start_f <- as.numeric(data_fusion$V7)
q.end_f <- data_fusion$V8
s.start_f <- data_fusion$V9
s.end_f <- data_fusion$V10

###################################################################################################

# DOT MATRIX AVEC LES SEGMENTS FUSIONES
plot(q.start[2], s.start[2], cex=.1, pch=1)
segments(q.start_f, s.start_f, q.end_f, s.end_f)

######################################################################################################

# FILTRER LA DOT MATRIX
plot(q.start[2], s.start[2], cex=.1, pch=1)
for(i in 1:length(q.start_f)){
  # valeur seuil arbitraire...
  if(abs(q.start_f[i]-q.end_f[i])>60000){
    segments(q.start_f[i], s.start_f[i], q.end_f[i], s.end_f[i])    
  }
}

