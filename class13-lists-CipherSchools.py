a = [1,2,3,4,5]
for x in a:
    print(x)

a = [1,2,4,5,3]
a.sort()
print(a)
b = [1,2,3,4,5]
print(list(reversed(b)))
a = [1,2,3,4,5]
for i, x in enumerate(a):
    pass

for x in map(lambda x: x**2 , a):
    print(x)

a = list(map(int , input().split(' ')))
print(a[0])
print(a)