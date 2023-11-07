# a='ne ok'
# b='ne'
# def olesya():
#     c= a.find(b)
#     if c!=-1:
#         print('есть контакт')
#     else:
#         print('мимо')
# olesya()

# a='всем приветикиприв'
# b=[]
# c='прив'
# s='нет ничего'
# def vika():
#     q=a.find(c)
#     if q==-1:
#         b.append(s)
#     else:
#         b.append(q)
#     w=a.rfind(c)
#     if w!=-1:
#         b.append(w)
#     print(b)
# vika()

# a='Обломов лежал лежал лежал и устал'
# from collections import Counter
# def sona(a):
#     f = Counter(a.replace(' ','')).most_common(3)
#     print(f)
# sona(a)

a='привет привет привет привет'

def anna(a):
    v = ''
    for i in range (len(a)):
        if i != len(a)-1:
            w = a[i]
            
            q = a[i+1]
            
            
            if w.islower() == True and q.islower() == True:
                
                b=a[i]
                v = v + b.swapcase()
                
            elif w.islower() == False and q.islower() == False:
                
                c=a[i+1]
                v = v + c.swapcase()  
        else:
            break
    print(v)
anna(a)

       
   # a.[0].swapcase() 
   # a.[0].islower()