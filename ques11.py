#question no 10 by ipsita sengupta
str=input("enter a string\n")
list1=list(str)
for x in list1:
    if x in"aeiou":
        list1.remove(x)
result=''.join(list1)
print(result)
