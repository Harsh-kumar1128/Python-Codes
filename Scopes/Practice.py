username = 'harsh'
def fun():
   # username = 'Python'
    print(username)
print(username)
fun()


x = 99
#def add(y):
 #   z = x+y
  #  return z
#print(add(1))

#def fun1():
 #   global x
  #  x =12

#fun1()
#print(x)

#def funmain():
    #x = 88
    #def f1():
       # print(x)
 #   f1()
#funmain()


def chaicoder(num):
    def actual(x):
        return x** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(3))
print(g(3))