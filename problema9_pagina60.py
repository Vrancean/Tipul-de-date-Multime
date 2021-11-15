x=int(input('nr de elemente din multimea A:'))
y=int(input('nr de elemente din multimea B:'))
A={str()}
B={str()}
for i in range(x):
    z=str(input('dati elementul din multimea A:'))
    if z>='A' and z<='Z':
        A.add(z)
for i in range(y):
    c=str(input('dati elementul din multimea B:'))
    if c>='A' and c<='Z':
        B.add(c)
print('intersectia=',A.intersection(B))
print('reuniunea=',A.union(B))
print('diferenta(A-B)=',A.difference(B))
print('diferenta(B-A)=',B.difference(A))