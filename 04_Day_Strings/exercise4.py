
# multi_str = ['Thirty', "Days", 'Of', 'Python']
# single_str = ' '.join(multi_str)
# print(single_str)

# multi_str = ['Coding', 'For', 'All']
# single_str = ' '.join(multi_str)
# print(single_str)

company = "Coding For All"
print(company)
print(len(company))

company = company.upper()
print((company.swapcase()).title()) #returns back to Coding For All

company = company.lower()
print(company)

company = company.title() #this is sufficient to return to Coding For All

#ex9
print(company[7:])

print(company.find('Coding', 7)) #returns -1 if not found
print(company.index('Coding')) #returns an error if not found

company = company.replace('Coding', "Python")
company2 = "Python for Everyone"
company2 = company2.replace('Everyone', "All")
print(company, company2)

company = 'Coding For All'
print(company.split()) #by default uses whitespace

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print((companies.split(', ')))

print(company[0])
print(company[-1])
print(company[(len(company) - 1)])
print(company[10]) #whitespace

company = 'Python For Everyone'
company2 = 'Coding For All'

#see if there is more a clever way to do this
company = company[0] + company[7] + company[11]
company2 = company2[0] + company2[7] + company2[11]
print(company)
print(company2)

print(company2.index('C'))
print(company2.index('F'))

sentence = 'You cannot end a sentence with because because because is a conjunction'
start = sentence.index('because') #31
end = sentence.rindex('because') #47
# sentence = sentence[0:start:end] is it possible to slice like this
sentence = sentence[0:start] + sentence[end+len('because'):]
print(sentence)
company2 = 'Coding For All'
print(company2.startswith('Coding'))
print(company2.startswith('coding'))

company2 = '   Coding For All      '
print(f"Length = {len(company2)} and original = {company2}")
company2 = company2.strip()
print(f"Length = {len(company2)} and after = {company2}")

identifier = '30DaysOfPython'
print(identifier.isidentifier())
identifier = 'thirty_days_of_python'
print(identifier.isidentifier())

python_libs = ['Django', 'Flask', 'Bottle', 'Pyramind', 'Falcon']
new_str = '# '.join(python_libs)
print(new_str)

#ex33
print(f"I am enjoying this challenge.\nI just wonder what is next.")

#ex34 - not quite right
print(f"Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#ex35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square")

a = 8
b = 6
print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {:.2f}'.format(a,b, a/b))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))







