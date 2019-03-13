data <- read.table("pestis_1348_co92_Alignment_hit_table.txt")
q.start <- data$V7
q.end <- data$V8
s.start <- data$V9
s.end <- data$V10

# donne un dot plot lisible
plot(q.start[2], s.start[2], cex=.1, pch=1)
for (i in 1:length(q.start)){
  # test des sens de lecture
  if(q.start[i]>q.end[i]){
    if(s.start[i]>s.end[i]){
      segments(q.start[i], s.start[i], q.end[i], s.end[i])    
    }
    else{
      segments(x0=q.start[i], y0=s.end[i], x1=q.end[i], y1=s.start[i])
    }
  }
  else{
    if(s.start[i]>s.end[i]){
      segments(x0=q.end[i], y0=s.start[i], x1=q.start[i], y1=s.end[i])    
    }
    else{
      segments(x0=q.end[i], y0=s.end[i], x1=q.start[i], y1=s.start[i])
    }
  }  
}

# idem avec des points
plot(q.start[2], s.start[2], cex=.1, pch=1)
for (i in 1:length(q.start)){
  # test des sens de lecture
  if(q.start[i]>q.end[i]){
    if(s.start[i]>s.end[i]){
      points(q.start[i], s.start[i], cex=.1)    
    }
    else{
      points(q.start[i], s.end[i], cex=.1)
    }
  }
  else{
    if(s.start[i]>s.end[i]){
      points(q.end[i], s.start[i], cex=.1)    
    }
    else{
      points(q.end[i], s.end[i], cex=.1)
    }
  }  
}


## Filtrer la dot matrix
plot(q.start[2], s.start[2], cex=.1, pch=1)
for(i in 1:length(q.start)){
  # valeur seuil arbitraire...
  if(abs(q.start[i]-q.end[i])>60000){
    # test des sens de lecture
    if(q.start[i]>q.end[i]){
      if(s.start[i]>s.end[i]){
        segments(q.start[i], s.start[i], q.end[i], s.end[i])    
      }
      else{
        segments(x0=q.start[i], y0=s.end[i], x1=q.end[i], y1=s.start[i])
      }
    }
    else{
      if(s.start[i]>s.end[i]){
        segments(x0=q.end[i], y0=s.start[i], x1=q.start[i], y1=s.end[i])    
      }
      else{
        segments(x0=q.end[i], y0=s.end[i], x1=q.start[i], y1=s.start[i])
      }
    }
    
  }
}
