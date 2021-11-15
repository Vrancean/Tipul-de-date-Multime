x=int(input('nr de elemente din multimea A:'))
y=int(input('nr de elemente din multimea B:'))
A={int(input('dati numerele multimii A:')) for i in range(x)}
B={int(input('dati numerele multimii B:')) for i in range(y)}
print('intersectia=',A.intersection(B))
print('reuniunea=',A.union(B))
print('diferenta(A-B)=',A.difference(B))
print('diferenta(B-A)=',B.difference(A))