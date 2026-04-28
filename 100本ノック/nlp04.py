l="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
list1=l.split()
list2=[]
w=""
for i in range(len(list1)):
    if i in (0,4,5,6,7,8,14,15,18):
       w=list1[i][:1]
       list2.append(w)
    else:
      w=list1[i][:2]
      list2.append(w)
print(list2)

dict1=dict(zip(list1,list2))
print(dict1)




