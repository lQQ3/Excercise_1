# Creat array "Num_Tails_until_Heads" with frames 0 - 10
Num_Tails_until_Head <- 0:10
# Create variable "Probabilty" and feed it a geometric probabilty distribution, (variable, probability)
Probabilty <- dgeom(Num_Tails_until_Head, 0.5)
# Show the data frame with column names
print(data.frame(Num_Tails_until_Head, Probabilty), row.names = FALSE, right=F)