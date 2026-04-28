#00
a="パトカー"
b="タクシー"
ab=a[0]+b[0]+a[1]+b[1]+a[2]+b[2]+a[3]+b[3]
print(ab)
#01
abs=ab[1]+ab[3]+ab[5]+ab[7]
print(abs)

#03
l="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list1=l.split()
print(list1)
list2=[]
list3=[]
for i in range(len(list1)):
    list2=list1[i]
    list3.append(list2[0])
print(list3)



