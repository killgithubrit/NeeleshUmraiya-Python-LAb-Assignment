from datetime import date 

today = date.today()

print(" Currennt year:", today.year)
print(" Currennt month:", today.month)
print(" Currennt day:", today.day)

d1 = today.strftime ("%d/%m/%y")
d2 = today.strftime ("%d/%y/%m")
d4 = today.strftime ("%y/%m/%d")

print(d1)
print(d2)
print(d4)


