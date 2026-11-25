a=input("enter your string::")
b=input("enter your string::")
if sorted(a)==sorted(b):
    print(f"{a} and {b} is an anagram string")
else:
    print(f"{a} and {b} is not an anagram string")