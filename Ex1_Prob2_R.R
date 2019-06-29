Total_Flips <- 10 # Declare number of flips
Heads <- 0:Total_Flips # Declare variable Heads and start it at 0
# Declare variable Probability as a binomial distribution, x axis of the data frame will be number of Heads
# with a 50% probability for each flip over Total_Flips number of flips
Probability <- dbinom(x=Heads, size = Total_Flips, prob = 0.5)
# create the output and title the columns Heads and Probability and fill them respectively
print(data.frame(Heads, Probability), row.names = FALSE, right=F)