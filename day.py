day=int(input("Enter the no. "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thrusday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Sunday")


    # method 2
# num = 0
# while True:
#     num = int(input("Enter a number between 1 and 7: "))
#     if 1 <= num <= 7:
#         break
#     else:
#         continue

# days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}

# print("The day is", days[num])