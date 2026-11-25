str=input("enter your string ::")
new_str=str.split()
largest=""
for i in new_str:
    if len(i)>len(largest):
        largest=i
print(f"largest string in the sentence is {largest}")
