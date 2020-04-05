def yhsj():
    row = [1]
    while True:
        yield(row)
        row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]
        #yield(row)
        #print(len(row),'\n')

n = 0
results = []
for t in yhsj():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)
