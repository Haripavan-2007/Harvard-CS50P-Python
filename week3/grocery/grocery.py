freq={}
try :
    while True:
        item=input()
        item=item.upper()
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
except EOFError:
    print()
    for x,y in sorted(freq.items()):
        print(y,x)
