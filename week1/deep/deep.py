num=str(input("What is the answer to the Great Question of Life, the Universe and Everything?"))
if num.strip()=="42":
    print("Yes")
elif num.strip().lower()=="forty two" or num.strip().lower()=="forty-two":
    print("Yes")
else:
    print("No")
