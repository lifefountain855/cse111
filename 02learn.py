from datetime import datetime

timeNow= datetime.now(tz=None)
# print(timeNow)
day=timeNow.weekday()
# print(day)

sub=float(input("Please enter the subtotal: "))
if (day == (1 or 2)):
    if (sub>=50.00):
        print(f"Discount amount: ${sub*0.1}")
        discounted=sub*0.9
        tax=discounted*0.06
        total=discounted+tax
    else: 
        print(f"It is Tuesday or Wednesday, but your subtotal {sub} is less than 50.00")
else : 
    tax=sub*0.06
    total=sub+tax
print(f"Sales tax amount: ${tax}")
print(f"Total: ${round(total,2)}")