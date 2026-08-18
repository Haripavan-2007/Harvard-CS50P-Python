def f2p(x):
    try:
        part=x.split("/")
        percent=(int(part[0])/int(part[1]))*100
        if 1<percent<99 :
            return str(round(percent))+"%"
        elif 0<=percent<=1:
            return "E"
        elif 99<=percent<=100:
            return "F"
        else:
            pass
            main()
    except (ValueError,ZeroDivisionError):
        main()
        pass
def main():
    fraction=input("Fraction :")
    print(f"{f2p(fraction)}")
main()

