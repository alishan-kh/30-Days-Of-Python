# Day 2: 30 Days of python programming

f_name = 'Alishan'
l_name = 'Khowaja'
full_name = f_name + ' ' + l_name
country = 'Pakistan'
city = 'Karachi'
age = 20
year = 2024
is_married = False
is_true = True
is_light_on = True
a, b ='1st alphabet', 2

# exercise Lv2
print(type(f_name))
print(type(l_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))

print(len(f_name))

print('is my first name longer than my lat name?', len(f_name) > len(l_name))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

pi= 22/7
# print(pi)
r = 3
area_of_circle = pi*(r**2)
# print(area_of_circle)
circum_of_circle = 2*pi*r
# print(circum_of_circle)

r = int(input('Input a value for radius'))
print('The area of the circle with radius ', r, 'is : ',(pi*(r**2)))

inp_fname = input('Enter your first name')
inp_lname = input('Enter your last name')
inp_country = input('Enter your Country name')
inp_age = int(input('Enter your Age'))

help('keywords')
