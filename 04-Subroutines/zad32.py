def f(n):
    n = int(n)
    if n <= 0:
        return "" 
    else:
        return "*/" * (n - 1) + "*" 
     
print(f(4))
print(f(1)) 
