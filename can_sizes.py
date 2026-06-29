"""
storage_efficiency = 
volume
surface_area
In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

volume = π*radius2*height
surface_area = 2π*radius(radius + height)


Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”

Name	Radius
(centimeters)	Height
(centimeters)	Cost per Can
(U.S. dollars)
#1 Picnic	6.83	10.16	$0.28
#1 Tall	7.78	11.91	$0.43
#2	8.73	11.59	$0.45
#2.5	10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	13.02	14.29	$0.83
#6Z	5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	15.72	17.78	$1.53
#211	6.83	12.38	$0.34
#300	7.62	11.27	$0.38
#303	8.10	11.11	$0.42
If you separate your program into functions, this problem will be much easier to solve than if you 
don't separate it into functions. You are free to write any functions that you choose in your 
program, but we strongly suggest that your program include at least these three functions:

main
compute_volume
compute_surface_area

Core Requirements
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
"""
import math
import csv

def main():
    strstr=''
    with open("12cans.csv", mode="r", newline="", encoding="utf-8") as c12_file:
        reader = csv.reader(c12_file)
        for row in reader:
            print(row)
            radius=float(row[1])
            height=float(row[2])
            vol=compute_volume(radius,height)
            suf=compute_surface_area(radius,height)
            strstr+=f'{row[0]}- Volume: {round(vol,2)}, Surface Area: {round(suf,2)}, Storage Efficiency: {round(vol/suf,2)}, Cost: {row[3]}\n'
            print(strstr)
            global prev ; prev = []
        print()
    return None

def compute_volume(radius,height):
    # computes the volume
    vol = math.pi*radius*2*height
    return vol

def compute_surface_area(radius,height):
    # computes the surface area
    suf = (2*math.pi)*radius*(radius + height)
    return suf

main()