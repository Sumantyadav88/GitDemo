'''str="Rahulshettyacademy.com"
str1="Consultingfirm"
str2="Rahulshetty"

print(str[1])    #Prints R

print(str[0:5])  #Prints Rahul

print(str+str1)  #concatenation

print(str2 in str)   #check one string in another string

var= str.split(".")   #splits string from "."

print(var)

print(var[0])  #prints Rahulshettyacademy'''

#**************************TRIM to Remove white spaces***********************************

str3 = "   Rahul   "

print(str3.strip()) #remove both left and right white spaces
print(str3.lstrip()) #remove left white spaces
print(str3.rstrip()) #remove right white spaces
