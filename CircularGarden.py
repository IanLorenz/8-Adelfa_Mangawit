import math

radius = float(input("Enter radius of your circular garden in meters: "))
area = math.pi * math.pow(radius, 2)
circumference = 2 * math.pi * radius
sr_area = math.sqrt(area)
rd_area = math.floor(area)
ru_area = math.ceil(area)

print(f"The area of your circular garden is {area: .2f} square meters.")
print(f"The circumference of uour circular garden is {circumference: .2f} meters")
print(f"The square root of the area of your circular garden is {sr_area:.2f} square meters")
print(f"The area rounded down of your circular garden is {rd_area:.2f} square meters")
print(f"The area rounded up of your circular garden is {ru_area:.2f} square meters")