from datetime import datetime
import math

width = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

volume = (math.pi * (width ** 2 )* aspect_ratio * (width * aspect_ratio + (2540*diameter))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters.")
if input("Would you like to buy these tires? (y/n) ").lower()=='y':
    phone_number=input("Great. What is your phone number? ")
else:
    print("That's too bad.")
    phone_number=None
now=datetime.now()

with open("output/volumes.txt", 'a') as volume_file:
    print(now,width,aspect_ratio,diameter,volume,phone_number, sep=", ", file=volume_file)
    print(f"Tire information recorded in {volume_file}")