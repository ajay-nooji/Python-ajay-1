N,X=map(int,input().split())
L=[]
for _ in range(X):
    L.append(map(float,input().split()))
for i in zip(*L):
    print('%.1f' %(sum(i)/X))