f = lambda x: x*56     # a lambda function   # lambda x: x*56  = known as anonymous function
print(f(23),f(3454))

# ACTUAL USAGE OF LAMBDA FUNCTIONS 


### MAP FUNCTIONS ###
x = [12,23,43,45,23,67,78,89]    # MAP OR MAPPING

x2 = list(map(lambda i:i**2,x))  # map function to print square 
print(x2)   

a = [1,2,3,4,45,5,68]
b = [2,4,6,78,9,34,7]
AB = list(map(lambda i,j:i*j ,a,b))
print(AB)

### FILTER() FUNCTION ### 
evens = list(filter(lambda i:i%2 == 0 , x))
print(evens)

