# Day 2: 30 Days of python programming

first_name = 'John'
last_name = 'Wick'
full_name = first_name + " " + last_name
print(full_name)
country = 'USA'
city = 'New York'
age = 39
year = 2026
is_married = False 
is_true = False
is_light_on = True
skills, num_friends = ['Shooting', 'Martial Arts'], 2 #one can define multiple variables in 1 line

#print can accept unlimited number of arguments theoretically speaking
print(
    type(first_name),"\n",
    type(last_name),"\n",
    type(full_name),"\n",
    type(country),"\n",
    type(city),"\n",
    type(age),"\n",
    type(year),"\n",
    type(is_married),"\n",
    type(is_true),"\n",
    type(is_light_on),"\n",
    type(skills),"\n",
    type(num_friends),"\n",
    )

print(len(first_name))
print(4 & 4) #4

is_equal = len(first_name) == len(last_name)
# is_equal = ((len(first_name) == len(last_name)) == 4) #True
print(is_equal) #True

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one 
exp = num_one**num_two
floor_division = num_one // num_two

#area
radius_m = 30
area_of_circle = 3.14 * radius_m**2 
print(area_of_circle)
#circumference
circum_of_circle = 2 * 3.14 * radius_m
print(circum_of_circle)

#area with user input
radius_user = input("Specify the circle radius=")
area_of_circle = 3.14 * float(radius_user)**2
print(area_of_circle)

#circumference with user input
circum_of_circle = 2 * 3.14 * float(radius_user)
print(circum_of_circle)

#get details
first_name = input('Enter first name=')
last_name = input('Enter last name=')
country = input('Enter the country=')
age = input('Enter the age=')
print(first_name, last_name, country, age)




