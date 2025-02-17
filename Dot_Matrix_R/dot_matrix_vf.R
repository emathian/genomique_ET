data <- read.csv("8F0EB0CW11N-Alignment-HitTable.csv", header=FALSE)
q.start <- data$V7
q.end <- data$V8
s.start <- data$V9
s.end <- data$V10

###############################################################################################

# DOT MATRIX (SANS LES SEGMENTS FUSIONES)
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000), xlab = "G??nome 1", ylab = "G??nome 2")
segments(q.start, s.start, q.end, s.end)

################################################################################################

# FILTRER LA DOT MATRIX (SANS LES SEGMENTS FUSIONES)
data_filtre=data[FALSE,]
n=length(q.start)
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000))
for(i in 1:n){
  # valeur seuil arbitraire
  if(abs(q.start[i]-q.end[i])>2000 | abs(s.start[i]-s.end[i])>2000){
    segments(q.start[i], s.start[i], q.end[i], s.end[i]) 
    data_filtre <- rbind.data.frame(data_filtre, as.data.frame(data[i,]))
  }
}

s.start=data_filtre$V9
s.end=data_filtre$V10
q.start=data_filtre$V7
q.end=data_filtre$V8


##############################################################################################    

# FUSIONER LES SEGMENTS TRES PROCHES (APRES AVOIR EFFECTUE UN PREMIER FILTRE)
data_fusion=data_filtre
n=length(q.start)
for(i in 1:n){
  for(j in 1:n){
    if(i!=j & data_fusion$V7[j]!=-1){
      if(((abs(s.start[j]-s.end[i]) < 5000 & abs(q.start[j]-q.end[i]) < 100000)) | (abs(s.start[j]-s.end[i]) < 100000 & abs(q.start[j]-q.end[i]) < 5000)){ 
        if(((s.end[j]-s.start[i])/(q.end[j]-q.start[i])-0.001) < (s.end[i]-s.start[i])/(q.end[i]-q.start[i]) & (s.end[i]-s.start[i])/(q.end[i]-q.start[i]) < ((s.end[j]-s.start[i])/(q.end[j]-q.start[i])+0.001)){
          # alors on fusionne les fragments i et j (qui deviennent un unique fragment i)
          data_fusion$V8[i]=data_fusion$V8[j] # q.end
          data_fusion$V10[i]=data_fusion$V10[j] #s.end
          data_fusion$V7[j]=-1 # q.start >> empêche la ligne j d'être considérée dans les boucles suivantes 

        }
      }
    }
  }
}


##################################################################################################

# SUPPRESSION DES LIGNES AVEC DES -1 
data_fusion=data_fusion[!grepl(-1, data_fusion$V7),]

q.start_f <- as.numeric(data_fusion$V7)
q.end_f <- data_fusion$V8
s.start_f <- data_fusion$V9
s.end_f <- data_fusion$V10

###################################################################################################

# DOT MATRIX AVEC LES SEGMENTS FUSIONES
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000))
segments(q.start_f, s.start_f, q.end_f, s.end_f)

######################################################################################################


# FUSIONER LES SEGMENTS TRES PROCHES (APRES UNE PREMIERE FUSION)
data_fusion2=data_fusion
for(k in 1:8){
  n=length(q.start_f)
  for(i in 1:n){
    for(j in 1:n){
      if(i!=j & data_fusion2$V7[j]!=-1){
        if(((abs(s.start_f[j]-s.end_f[i]) < 10000*k & abs(q.start_f[j]-q.end_f[i]) < 100000)) | (abs(s.start_f[j]-s.end_f[i]) < 100000 & abs(q.start_f[j]-q.end_f[i]) < 10000*k)){ # seuil arbitraire inferieur au 1er quartile de abs(s.start-s.end)
          if(((s.end_f[j]-s.start_f[i])/(q.end_f[j]-q.start_f[i])-0.01) < (s.end_f[i]-s.start_f[i])/(q.end_f[i]-q.start_f[i]) & (s.end_f[i]-s.start_f[i])/(q.end_f[i]-q.start_f[i]) < ((s.end_f[j]-s.start_f[i])/(q.end_f[j]-q.start_f[i])+0.01)){
            # alors on fusionne les fragments i et j (qui deviennent un unique fragment i)
            data_fusion2$V8[i]=data_fusion2$V8[j] # q.end
            data_fusion2$V10[i]=data_fusion2$V10[j] #s.end
            data_fusion2$V7[j]=-1 # q.start >> empeche la ligne j d'etre consideree dans les boucles suivantes 
          }
        }
      }
    }
  }
  
  ##################################
  
  # SUPPRESSION DES LIGNES AVEC DES -1 
  data_fusion2=data_fusion2[!grepl(-1, data_fusion2$V7),]
  
  q.start_f <- as.numeric(data_fusion2$V7)
  q.end_f <- data_fusion2$V8
  s.start_f <- data_fusion2$V9
  s.end_f <- data_fusion2$V10
}
###################################################################################################

# DOT MATRIX AVEC LES SEGMENTS FUSIONES
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000), xlab = "G??nome 1", ylab = "G??nome 2")
segments(q.start_f, s.start_f, q.end_f, s.end_f)


##################################################################################################

# FILTRAGE FINAL DE LA DOT MATRIX
data_filtre_fin=data_fusion[FALSE,]
plot(q.start[25], s.start[25], cex=.1, pch=1, xlim =c(0, 5000000), ylim = c(0, 5000000), xlab = "G??nome 1", ylab = "G??nome 2")
n=length(q.start_f)
for(i in 1:n){
  # valeur seuil arbitraire
  if(abs(q.start_f[i]-q.end_f[i])>20000 | abs(s.start_f[i]-s.end_f[i])>20000){
    segments(q.start_f[i], s.start_f[i], q.end_f[i], s.end_f[i])
    data_filtre_fin <- rbind.data.frame(data_filtre_fin, as.data.frame(data_fusion[i,]))
  }
}

######################################################################################################

# COMPARAISON TAUX DE SIMILARITE

# CHEZ LES ALIGNEMENTS GARDES
taux_garde = mean(data_filtre_fin$V3)

# CHEZ LES ALIGNEMENTS NON GARDES
taux_non_garde = mean(data_non_garde$V3)

###########################################################################
# EXPORTATION DES DONNEES

q.start_f <-data_filtre_fin$V7
q.end_f <- data_filtre_fin$V8
s.start_f <- data_filtre_fin$V9
s.end_f <- data_filtre_fin$V10


data = data.frame(Qstart = q.start_f , Qend = q.end_f,Sstart = s.start_f , Send = s.end_f)
data = data[order(data$Qstart),]
data["ID"]=  seq(1:length(q.start_f))
data

data_orga_ref = data.frame(Qstart = data$Qstart , Qend = data$Qend , ID=data$ID)

data_orga_interest = data.frame(Sstart = data$Sstart , Send =data$Send , ID=data$ID)
data_orga_interest = data_orga_interest[order(data_orga_interest$Sstart),]
data_orga_interest


write.table(data_orga_ref, "data_orga_ref.txt", append = FALSE, sep = "\t", dec = ".", quote=FALSE,col.names = TRUE, row.names = FALSE)
write.table(data_orga_interest, "data_orga_interest.txt", append = FALSE, sep = "\t", dec = ".", quote=FALSE,col.names = TRUE, row.names = FALSE)

