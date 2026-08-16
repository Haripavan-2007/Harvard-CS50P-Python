def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<=len(s)<=6:
        if s[:2].isalpha():
            for i in range(2,len(s)):
                if s[i].isalpha():
                    pass
                elif s[i].isdigit():
                    if s[i]!="0":
                        if s[i:].isdigit():
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return True
        return False
    else:
        return False


main()
