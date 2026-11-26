s=input("enter your string")
str=s.split()

for i in str:
    print(i[0].upper() + i[1:], end=" ")
