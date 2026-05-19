x="paraparaparadise"
y="paragraph"
def ngram(li,n):
    ngramlist=[]
    for i in range(len(li)-n+1):
        p=""
        for m in range(n):
              p+=li[i+m]
        ngramlist.append(p)
    return ngramlist

resultx=set(ngram(x,2))
resulty=set(ngram(y,2))
i=resultx.union(resulty)
print(i)
j=resultx&resulty
print(j)
k=resultx-resulty
print(k)

def check(p):
    for i in range(len(p)):
        if p[i]=="se":
            return print("seが含まれている")
list_i=list(i)
z=check(list_i)
print(z)


