greet=input("Greetings :")
if "hello" in greet.lower():
    print("$0")
elif greet.strip()=="":
    print("$0")
elif greet.strip().lower()[0]=="h":
    print("$20")
else:
    print("$100")
