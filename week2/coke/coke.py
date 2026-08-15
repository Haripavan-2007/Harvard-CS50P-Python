amount_due=50
denomination=[5,10,25]
while amount_due>0:
    print("amount due:",amount_due)
    pay=int(input("Insert coin:"))
    amount_due-=pay if pay in denomination else 0
print("Change owed:",amount_due*-1)
