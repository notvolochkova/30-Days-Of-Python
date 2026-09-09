
my_age = 18
my_height = 176
complex_a = 1 + 2j

#compute the area of a triangle
# base = float(input("Enter the base ="))
# height = float(input("Enter the height="))
# area = base * height * 0.5
# print("Option 2: Area of a triangle=", area)

#compute the perimeter
# a = float(input("Enter side a="))
# b = float(input("Enter side b="))
# c = float(input("Enter side c="))
# perimeter = a + b + c
# print(f"Perimeter of the triangle = {perimeter:.4f}")

#area of a rectangle
# length = float(input("Enter the length="))
# width = float(input("Enter the width="))
# area = length * width 
# print(f"area of the rectangle = {area:.4f}")

# #perimeter of the rectangle
# length = float(input("Enter the length="))
# width = float(input("Enter the width="))
# perimeter = 2 * (length + width)
# print(f"perimeter of the rectangle = {perimeter:.4f}")

#area of a circle
# radius = float(input("Enter the radius ="))
# area = 3.14 * radius **2
# circumference = 2 * 3.14 * radius
# print(f"Area of the circle = {area:.2f}, Circumference = {circumference:.2f}")

#calculate the slope of line equation and x,y intercept values
#if x-intercept y = 0, if y-intercept x = 0
# y = 2x - 2, slop = 2, x-intercept = 1, y-intercept = -2
m_1 = 2

#calculate the slope from 2 coordinates 
#(2,2) and (6,10)
# x_1 = 2
# y_1 = 2
# x_2 = 6 
# y_2 = 10
# m_2 = (y_2 - y_1) / (x_2 - x_1)
# import math
# euclidean_distance = math.sqrt(((x_2 - x_1)) ** 2 + ((y_2 - y_1) ** 2))
# print(f"Slope m_1 = {m_1}, Slope m_2 = {m_2}, Euclidean distance = {euclidean_distance}")

# #comparing the slope values
# if m_1 == m_2:
#     print(f"Slope 1 and Slope 2 are the same values")
# elif m_1 <= m_2:
#     print(f"Slope 1 <= Slope 2")
# elif m_1 >= m_2:
#     print(f"Slope 1 > Slope 2")
# else:
#     print(f"No condition satisfied")

# print(f"Length of the word `dragon` and `python` are same? = {len("python") == len("dragon")}")
# print("`on` is inside dragon and python both? =", "on" in "python" and "dragon")
# print("Is `jargon` present in the statement ? =", "jargon" in "I hope this course is not full of jargon")
# print("There is no `on` inside `python` and `dragon` both right? =","on" not in "python" and "dragon")
# str_len = len("python")
# print("Now is what? = ", type(str_len))
# print("Now in float = ", type(float(str_len)))
# print("Now in int = ", type(str(str_len)))

# your_number = int(input("Enter your number to determine if odd or even = "))
# if (your_number % 2 != 0):
#     print(f"Your number is odd and has remainders = {your_number % 2}")
# else:
#     print(f"Your number is even and divisible by 0")

# print("Is the floor divison equal of 7//3 == int(2.7)?? ", 7//3 == int(2.7))
# print("Are types equal ??", type('10') == type(10)) #nope, string != int
# print("int('9.8') == 10 ??", int(float('9.8')) == 10)

# total_hours = float(input("How many hours have you worked ??"))
# rph = float(input("What is your rate per hour (RPH)??"))
# print(f"Your weekly earning is = {total_hours * rph:.2f}")

'''
1hr = 3600s
1 day = 86400s
1 year = 31536000s
'''
#years lived is usually as whole number
# years_lived = int(input("Enter the number of years you have lived"))
# ONE_YEAR_SEC = 31536000
# seconds_lived = ONE_YEAR_SEC * years_lived
# print(f"You have lived for {seconds_lived} seconds.")

#both give same answer which is better? option assuming DRY principle
for i in range(1,6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")

for i in range(5):
    print(f"{(i+1)} {(i+1)**0} {(i+1)**1} {(i+1)**2} {(i+1)**3}")




