"""#list data types
l=[5, 23,3,"Rahul",4,8]
l.append("Sumant") #element add at last

l[2]=(70) #updation
del l[2] #deletion
print(l)

#Tuple- Same as List but updation not allowed

a=(2,4,52,2312,"Sumant") #It is a tuple
print(a)
#a[2] = 12 #cannot update this

#Dictionary
u= {1:"Sumant",2:"Yadav"}
print(u[1], u[2])

t= {"a":"Hemant","b":"Yadav"}
print(t["a"], t["b"])

# if else Condition

a=12
b="Sumant"
c="Aakrati"
d="18"
if a<15 and b=="Sumant":
    print("TRUE")
else:
    print("False")
print("Thanku")

# FOR LOOP
list=[2,5,8,6,4,9]

for i in list:
    print(i)

#sum of first 5 natural numbers
add = 0
for j in range(1, 6): # 1 is inclusive and 6 is exclusive
    add = add+j
print(add)

# In Range(initial index, last index, jump in index)

for m in range(1,10,2):
    print(m)
# if initial index in not present it is by default 0 and jump in index is by default"""

#*********************************WHILE LOOP**********************************************************

w = 20
while w > 15:
    if w==18:
        w=w-1
        continue #stop the current iteration and do the next one
    if w==16:
        break #it breaks the while loop immediately
    print(w)
    w = w-1
print("while loop execution done")
