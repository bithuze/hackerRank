from collections import defaultdict

n,m=map(int,input().split())
g_a= [input().strip() for _ in range(n)]
g_b= [input().strip() for _ in range(m)]

d = defaultdict(list)
for inex,word in enumerate(g_a,1):
    d[word].append(inex)
for i in g_b:
    if i in d:
        print(' '.join(map(str, d[i])))
    else:
        print(-1)
