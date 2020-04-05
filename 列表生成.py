L=['Hello','World',18,'Apple',None]
print(list(s.lower() for s in L if isinstance(s,str)))
#isinstance(x,str)是内建函数,判断x是不是str类型,如果是返回True
