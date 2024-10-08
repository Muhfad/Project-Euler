'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# factorial grows much faster than additions. Put a bound on the number of digits
# Can we think of the problem in terms of Problem 31 where the we consider a currency
system where the denominations are from 1 to 9! and we are seeking for numbers 
which are equal to some ordering of the digits its representation including repeats. 
'''

#%%
from math import factorial
from math import comb

fact = {i:factorial(i) for i in range(10)}

# %%
# fig, axs = plt.subplots(2, 1)
# axs[0].set_xlabel('yes')
# axs[0].legend() 
# axs[0].vlines(10)
# plt.show()
