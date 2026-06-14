#movie tickets pricing

Age = int(input("Enter the age"));
day = "Wednesday"

price  = 12 if Age >= 18 else 8

if day == "Wednesday":
    price = price - 2

print("Ticket price for you",price)