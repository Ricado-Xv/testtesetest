from functools import reduce
#def fn(x,y):
#    return x*10+y
#def charTonum(s):
#    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#    return digits[s]

#result=reduce(fn,map(charTonum,'12345'))
##reduce()把一个函数作用在一个序列上
##map()把一个函数依次作用在序列的每个元素上
#print(result )
def normalize(name):
    x=[]
    list_name=list(name)
    for i in list_name:
        if i is list_name[0]:
            list_name[0]=None
            if i.isupper():
                x=x+list(i)
                continue
            else:
                i=i.upper()
                x=x+list(i)
                continue
        if i is not list_name[0]:
            if i.isupper():
                i=i.lower()
                x=x+list(i)
            else:
                x=x+list(i)
    return x
result=list(map(normalize,['adam','LISA']))
print(result)
