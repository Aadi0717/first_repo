#logical AND operator
a=8
b=9
c=4
print(a==b & a==c)
print(a!=c & b!=c)
print(c>b & b>a)
print(a<b & a<c)
print(a<=c & b>=a)
print(a>=b & c>=a)

#logical OR operator
print(a==b | a==c)
print(a!=c |  b!=c)
print(c>b  |  b>a)
print(a<b  | a<c)
print(a<b | c>a)
print(a<=c |b>=a)
 
 #relataional NOT operator
 
print(not(a==c))
print(not(b!=c))
print(not( b>a))
print(not (a>c))
print(not (a==b & b==c))
 