expression=input("Exprersion :")
x,y,z=expression.split()
match y:
    case "+":
        print(f"{float(int(x)+int(z)):.1f}")
    case "-":
        print(f"{float(int(x)-int(z)):.1f}")
    case "*":
        print(f"{float(int(x)*int(z)):.1f}")
    case "/":
        if z!="0":
            print(f"{float(int(x)/int(z)):.1f}")
        else:
            print("Can't devided by zero")
