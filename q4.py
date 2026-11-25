str=input("enter your string ::")
new_str=""
for i in str:
    if i not in new_str:
        new_str=new_str+i
print(new_str)        