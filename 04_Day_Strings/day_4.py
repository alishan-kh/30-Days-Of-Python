to_join = ['Thirty' , 'Days' , 'Of' , 'Python']
print(' '.join(to_join))

to_join1 = ['Coding' , 'For' , 'All']
print(' '.join(to_join))

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
first_word = company.split()[0]
print(first_word)

if 'Coding' in company:
    print('Word found at ',company.index('Coding'))
else:
    print('Word not found in the string')
found = company.find('Coding')

new_company = company.replace('Coding', 'Python')

new_company = company.replace('Everyone', 'All')

splitted_company = company.split() # by default the value inside split() is ' '

figma = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
splitted_figma = figma.split(',')

print(company[0])

print(len(company)-1)

print(company[10])

acronym = "".join(new_company[0].upper() for new_company in new_company.split()) #splitting the string word by word then capitalizing the first index of the remaining string and appending it into a strong called acronym to make an abbreviation

acronym1 = ''.join(company[0].upper() for company in company.split())

position_c = company.index('C')

position_f = company.index('F')

last_I = company.rfind('I')

sentence = 'You cannot end a sentence with because because because is a comjuction'
position_because = sentence.index('because')

last_because = sentence.rindex('because')

sliced = sentence[sentence.index('because'):sentence.rindex('because')+len('because')] #upper limits in python are exclusive so we had to add the length of the word 'because' in order to slice out all 3 occurances of the word instead of only the first 2

print(company.startswith('Coding'))

print(company.endswith('coding'))

print(company.strip())

''' 
30DaysOfPython will return false when we use the isidentifier() method as an identifier cant start with a number
while thirty_days_of_python will return True
'''
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print(' #'.join(libraries))

print('I am enjoying this challenge.\nI just wonder what is next')

print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print(f'The are of the circle with radius 10 is {area}')

print(f'8 + 6 = {14}\n8 - 6 = {8-6}\n8 * 6 = {8*6}\n8 / 6 = {8/6}\n8 % 6 = {8%6}\n8 // 6 = {8//6}\n8 ** 6 = {8**6}\n')
