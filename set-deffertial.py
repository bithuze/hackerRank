l=int(input())
engliz=list(input().split())
m=int(input())
frenchwa=list(input().split())
en=set(engliz)
fr=set(frenchwa)

print(len(en.difference(fr)))
