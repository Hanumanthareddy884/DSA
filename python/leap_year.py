year = int(input("Enter year = "))


if year % 400==0 and year % 100==0 or year % 4 ==0:
    print("{0} is lear year".format(year))
else:
    print("Not leap year")