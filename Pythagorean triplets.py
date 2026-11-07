n = int(input("N= "))
count = 0

for a in range(1,n+1):
  for b in range(1,n+1):  #we can also change range as (a,n+1) so that the values won't repeat.
    
    c_square = (a**2 + b**2)
    c = int(c_square**0.5)
    
    if c_square == c**2 and c<=n:
      print(a,b,c)
      count += 1
      
print(count)
