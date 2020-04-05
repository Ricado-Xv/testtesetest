for x in [1,2,3,4,5]:
    print(x)

print('\n')

it=iter([1,2,3,4,5])
while True:
    try:
        x=next(it)
        print(x)
    except StopIteration as e:
        print('Catch generator finished:',e.value)
        break
