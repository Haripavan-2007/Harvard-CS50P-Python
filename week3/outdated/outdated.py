months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date: ")#MM/DD/YYYY or #month DD, YYYY
        if date[0].isalpha():#month DD, YYYY ---> YYYY-MM-DD
            date=date.strip().split()
            month=date[0].title()
            if month in months and int(date[1][:-1])<32:
                print(f"{date[2]}-{months.index(month)+1:02}-{int(date[1][:-1]):02}")
                break
            else:
                pass
        else:#MM/DD/YYYY ---> YYYY-MM-DD
            date=date.strip().split("/")
            if int(date[0])<13 and int(date[1])<32:
                print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")
                break
            else:
                pass
    except:
      pass
