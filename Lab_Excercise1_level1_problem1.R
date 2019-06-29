#title: "exercise1_shawnRice"
#author: "Shawn Rice"
#date: "April 26, 2018"
#output: html_document

# Draw some random numbers from the normal distribution
N <- 1000 # N is a constant which equals 1000
n <- 100 # n is a constant which equals 100
x <- rnorm(N) # Generates a random number from the normal distribution (N) times
x1 <- runif(n) # Generates a random number from eth uniform distribution (n) times

# Plot a histogram
hist(x, freq = FALSE) # freq=FALSE changes the plot from frequency to density

# Get the x & y values of a normal curve fitted to these random numbers
x_fit <- seq(min(x), max(x), length=N*10) # Generate a sequence of the graph of N number of points, x10 at number of points to smooth the curve 
y_fit <- dnorm(x_fit, mean = mean(x), sd=sd(x)) # Density values from normal distribution for x_fit and assign them to the y axis
x1_fit <- seq(min(x), max(x), length=n*10)
y1_fit <- dnorm(x1_fit, mean=mean(x1), sd=sd(x1)+1)

par(mfcol=c(1,2))
plot(x_fit, y_fit)
plot(x1_fit, y1_fit)
#lines(x_fit, y_fit) # Graph it
#lines(x1_fit, y1_fit)