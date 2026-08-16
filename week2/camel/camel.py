var=input("camelcase:")
snake_case=[]
for ch in var:
    if ch.islower():
        snake_case.append(ch)
    else:
        snake_case.extend(["_",ch.lower()])
print("".join(snake_case))


