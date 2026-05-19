word="sakana"
w_list=list(word)
ascii=[]
def cipher(w):
    for i in w:
      if 'a' <= i <= 'z':
         ascii.append(ord(i))
    return ascii
    return w

print(cipher(w_list))

