#def sum_all(*char):
def sum_all(*args):
   # return sum(char)
    print(args)
    for i in args:
        print(i*2)
    return sum(args)
#print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))