#Day 3: 30 Days of python programming
age = 20
height = 5.11
num_complex = 4-4j

#Enter Base and Height of a triangle
triangle_base = float(input('Input Base of a triangle : '))
triangle_height = float(input('Input Height of a triangle : '))
print('Area of the triangle with entered Base and Height is : ',0.5*triangle_base*triangle_height)

#Enter Sides of a triangle
side_a = float(input('Input Side A : '))
side_b = float(input('Input Side B : '))
side_c = float(input('Input Side C : '))
print('The perimeter of the triangle is : ',side_a+side_b+side_c)

#Enter Sides of a Rectangle
rect_len = float(input('Input rectangle length : '))
rect_width = float(input('Input rectangle widht : '))
print('The area of the rectangle is : ',rect_len*rect_width)
print('The perimeter of the rectangle is : ',(2*rect_len)+(2*rect_width))

#Enter Radius of a triangle
pi= 3.14
triangle_radius = float(input('Enter radius : '))
print('the radius of the triangle is : ',pi*triangle_radius*triangle_radius)
print('the circumference of the triangle is : ',2*pi*triangle_radius)

m8 = 2
m9 = (10-2)/(6-2)
ed9 = (((6-2)**2)+((10-2)**2))**0.5

print('Is the slope in q9 greater than, less than or equal to the one in q8? ')
if m9>m8:
    print('Greater Than')
elif m9==m8:
    print('Equal to')
else:
    print('Less than')

for x in range(-5,5):
    if ((x**2)+(6*x)+9)==0:
        print('The value of X for which y is 0 : ',x)

print('length of the word "python" : ',len('python'))
print('length of the word "dragon" : ',len('dragon'))
print('length of the words python and dragon are not equal.',len('dragon')!=len('python'))

if 'on' in 'python' and 'dragon':
    print('True, "on" is present in both')
    
if 'jargon' in 'I hope this course is not a jargon':
    print('True, "Jargon" is present in the sentence')

if 'on' not in 'python' and 'dragon':
    print('True, "on" is not present in both')
else:
    print('False, "on" is present in both')

str(float(len('python')))

#to check for even or odd, we use modulus 2 --> x%2, if the answer is 0 it means the number is even hence there is no remainder, else the number is odd.

print((7//3)==int(2.7))
print(type('10')==type(10))
print(int(9.8)==10)

hours = input('enter hours ')
rph = input('enter rate per hour ')
print('weekly earning is = ',int(rph)*int(hours))

years = input('number of years youve lived ')
print('youve lived for ',365*24*60*60*int(years), ' seconds')

for i in range(1,6):
    print(f'{i} 1 {i} {i*i} {i*i*i}')
