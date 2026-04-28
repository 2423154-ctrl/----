l="I am an NLPer"
list1=l.split()
list2=list(l)



def ngram(li,n):
    ngramlist=[]
    for i in range(len(li)-n+1):
        p=""
        for m in range(n):
              p+=li[i+m]
        ngramlist.append(p)
    return ngramlist
       
result1=ngram(list1,2)
print(result1)
result2=ngram(list2,3)
print(result2)
   

    




