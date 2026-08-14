def main():
    t=input("What time is it?")
    t=convert(t)
    if 7<=t<=8:
        print("breakfast time")
    elif 12<=t<=13:
        print("lunch time")
    elif 18<=t<=19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours,minutes=time.split(":")
    time=float(hours)+float(minutes)/60
    return time
if __name__ == "__main__":
    main()




