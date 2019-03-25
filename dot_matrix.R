data <- read.table("pestis_1348_co92_Alignment_hit_table.txt")
q.start <- data$V7
q.end <- data$V8
s.start <- data$V9
s.end <- data$V10

# donne un dot plot lisible
plot(q.start[2], s.start[2], pch=4)
for (i in 1:length(q.start)) {
  
  segments(q.start[i], s.start[i], q.end[i], s.end[i])
}

plot(q.start[2], s.start[2],cex=.3)
for (i in 1:length(q.start)) {
  points(q.start[i], s.start[i], cex=.3)
}

plot(q.start, s.start, cex=.3)
