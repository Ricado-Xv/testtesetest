def findMinandMax(L):
    if L==[]:
        #return (None,None)
        Min=None
        Max=None
    else :
        Min=L[0]
        Max=L[0]
        for i in L:
            if i<Min:
                Min=i
            if i>Max:
                Max=i
    print(Min,Max)
