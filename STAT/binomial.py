import numpy as np
from scipy.special import comb

# Could build a more robust, polymorphism based discrete random variable program, but this is quick and dirty.

# Function to compute the probability of binomial random variable == a value v.
def bin_pmf(n,p,v):
    return int(comb(n,v))*(p**v)*((1-p)**(n-v))

# Function to compute probability accumulated across multiple valuess == cdf of binomial random variables.
# Returns probability of a binomial RV's value being <= v from start.
def bin_cdf(n,p,start,v):
    sum = 0
    for i in range(start, v+1):
        sum += bin_pmf(n,p,i)
    return sum

# Probability of "success" on each "toss"
p = 0.9082
# Number of tosses/independent trials
n = 100

# For HW9, #5.24:
result = bin_cdf(n,p,0,19)
print(result)