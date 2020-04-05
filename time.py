import time
import calendar as cal

#ticks=time.time()
#print(ticks)

#localtime=time.localtime(time.time())

#标准格式化
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

#日历
print(cal.month(2019, 3))

print(time.perf_counter())
