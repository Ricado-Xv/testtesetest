import math
def quadratic(a,b,c):
    m=b**2-4*a*c
    x1=(-b+math.sqrt(m))/(2*a)
    x2=(-b-math.sqrt(m))/(2*a)
    return x1,x2
#自定义函数返回多个值,是以tuple的方式返回的,取用的时候,按照tuple里的顺序取出
