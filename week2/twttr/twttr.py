twttr=input("Input:")
vowels="aeiouAEIOU"
output=""
for ch in twttr:
    if ch not in vowels:
        output+=ch
print("Output:",output)
