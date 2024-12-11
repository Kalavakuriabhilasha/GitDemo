def max(a,b):
    if a>b:
        return a
    else:
        return b

a=2
b=4
print(max(a,b))

#----------

int1=3
int2=4

maximumnum = max(int1,int2)
print(maximumnum)

#------------------
c=5
d=2

print(c if c >= d else d)

#---------

e = 5
f = 4
x = [e, f]  # Create a list containing a and b
x.sort()  # Sort the list in ascending order
print(x[-1]) # -1 will start from last