s = "don't()mul(7,8)"

dosplit = s.split("do()")

for i in dosplit:
    dontsplit = i.split("don't()")
    print(dontsplit[0])

