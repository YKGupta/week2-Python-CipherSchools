#tuples class 14
a = (1,2,3,4,5)
print(type(a))

def func(*args):
    print(type(args))
func(1,2,3,4,5)

a= 5
b= 9
a,b = b,a
c = a,b
type(c)

def sum_diff(a,b):
    s = a+b
    d = a-b
    return s,d

a = [1,2,3,4,5]
print(list(range(5)))
print(tuple(range(5)))

a = [1,2,3,4,5]
a.append(5) 
print(a)
a = {"name" : "Yash Kumar Gupta", "company" : "Google", "college" :  "LPU"}
key = "marks"
print(a.get(key, "Key doesn't exist"))