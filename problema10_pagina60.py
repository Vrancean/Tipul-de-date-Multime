A={1,2,3,4}
B=[[]]
for i in A:
    B+=[k+[i] for k in B]
print(sorted(B))