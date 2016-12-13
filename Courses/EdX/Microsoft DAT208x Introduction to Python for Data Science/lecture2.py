#Lists
a=["a", 3.14, "b", 1.999, "c", 10]

print(a)
#indexing lists:
#2nd element
print(a[1])
#3rd element from end of list
print(a[-3])
#slicing:
#from index 2 (inclusive) to index 4 (exclusive) 
print(a[2:4])
#from start:
print(a[:4])
#until end:
print(a[2:])

#removing an element (4th) from a list:
del(a[3])
print(a)

#Adding an element to a list:
a = a + ["added at the end"]
#Copying lists:
#a only contains a reference to the actual list, so modifying b affects a also
b = a
b[1] = 3.14159
print(a)

#for an explicit copy of the list content:
c = list(a)
#or:
d = a[:]

c[3] = 123
d[3] = 456

print(a)