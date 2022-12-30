#file = open('test.txt')

'''print(file.read(7))

print(file.readline())
print(file.readline())



#print line by line using readline method of full file

line = file.readline()
while line!= "":
    print(line)
    line = file.readline()

#one more method

#file.readlines()

for line in file.readlines():  #For Loop
    print(line)

file.close()'''

#Read the file and store all in the list
#Reverse the list
#write the list back into file

#another way of opening a file ------------------DOUBT

with open('test.txt', 'r') as reader:
    content= reader.realines()  #Initial list
    reversed(content)   #reversed list
    while open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)



