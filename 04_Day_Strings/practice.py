
# letter = 'p'
# print(letter)
# print(len(letter))

# greeting = 'Hello, World!'
# print(greeting)
# print(len(greeting))
# sentence = "I hope you are engjoing 30 days of Python challenge"
# print(sentence)

# #multi-line strings are also a thing
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# multiline_string = """I am a teacher and the stuff again"""
# print(multiline_string)

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# space = ' '
# full_name = first_name + space + last_name
# print(full_name)
# print(len(first_name))
# print(len(last_name))
# print(len(first_name) > len(last_name))
# print(len(full_name))


# print('I hope everyone is enjoying the Python Challenge.\nAre you?')
# print('Days\tTopics\tExercises')
# print('Day 1\t5\t5')
# print('day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash symbol (\\)')
# print('In every programming language it starts with \"Hello, World!\"')

# first_name = 'Asabeneh'
# last_name = 'Yetyayeh'
# language = 'Python'
# formatted_str = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formatted_str)

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formatted_str = 'The area of a circle with a radius is %d is %.2f' %(radius, area)
# print(formatted_str)

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
# formatted_str = 'The following are python libraries:%s' %(python_libraries)
# print(formatted_str)

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formatted_str = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
# print(formatted_str)
# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a,b,a-b))
# print('{} * {} = {}'.format(a,b,a*b))
# print('{} / {} = {}'.format(a,b,a/b))
# print('{} % {} = {}'.format(a,b,a%b))
# print('{} // {} = {}'.format(a,b,a//b))
# print('{} ** {} = {}'.format(a,b,a**b))

# radius = 10 
# pi = 3.14
# area = pi * radius **2
# formatted_str = 'The area of circle with a radius {} is {:.2f}'.format(radius, area)
# print(formatted_str)

# a = 4
# b = 3
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b:.2f}")
# print(f"{a} % {b} = {a%b}")
# print(f"{a} // {b} = {a//b}")
# print(f"{a} ** {b} = {a**b}")

#string as seq of characters
# language = 'python'
# a,b,c,d,e,f = language #unpacks

# for i in [a,b,c,d,e,f]:
#     print(i)

# language = 'Python'
# first_letter = language[0]
# print(first_letter)

# second_letter = language[1]
# print(second_letter)

# last_index = len(language) - 1
# last_letter = language[last_index]
# print(last_letter)

# last_letter = language[-1]
# print(last_letter)
# second_last = language[-2]
# print(second_last)

# language = 'Python'
# first_three = language[0:3] #Pyt
# print(first_three)

# last_three = language[3:6] #hon
# print(last_three)

# last_three = language[-3:] #hon
# print(last_three)

# last_three = language[3:] #hon
# print(last_three)

# greeting = 'Hello, World!'
# print(greeting[::-1])

# language = 'Adenosine Triphosphate (ATP)'
# pto = language[0:6:2]
# print(pto)

# challenge = 'thirty days of python'
# print(challenge.capitalize())
# print(challenge.count('y'))
# print(challenge.count('y', 7, 14)) #returns ' days of' so only 1 occurence
# print(challenge.count('th'))

# print(challenge.endswith('on'))
# print(challenge.endswith('tion'))

# challenge = 'thirty\tdays\tof\tpython'
# print(challenge.expandtabs())
# print(challenge.expandtabs(10))
# print(challenge.find('y'))
# print(challenge.find('th'))
# print(challenge.rfind('y'))
# print(challenge.rfind('th'))

# first_name = 'Asabeneh'
# last_name  = 'Yetayeh'
# age = 250
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}'.format(first_name, last_name, job, age, country)
# print(sentence)

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
# print(result)

# challenge = 'thirty days of python'
# sub_string = 'da'
# print(challenge.index(sub_string))
# print(challenge.index(sub_string, 9)) #returns an error


# challenge = 'thirty days of python'
# sub_string = 'da'
# print(challenge.rindex(sub_string))
# print(challenge.rindex(sub_string, 9))
# print(challenge.rindex('on', 8))

# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum())

# challenge = '30DaysPython'
# print(challenge.isalnum())

# challenge = 'thirty days of python'
# print(challenge.isalnum())

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum())

# challenge = 'thirty days of python'
# print(challenge.isalpha())

# challenge = 'ThirtyDaysPython'
# print(challenge.isalpha())

# num = '123'
# print(num.isalpha())

# challenge = '30ThirtyDaysOfPython'
# print(challenge.isalpha())

# challenge = 'thirty days of python'
# print(challenge.isdecimal())

# challenge = '123'
# print(challenge.isdecimal())

# challenge = '\U0001F600' #False cuz its an emoji
# print(challenge.isdigit())

# challenge = '\u00B2'    #True cuz represents a digit 2
# print(challenge.isdigit())

# print(challenge.isdecimal()) #False

# challenge = '12 3'
# print(challenge.isdecimal()) #False

# num = '10'
# print(num.isnumeric())
# num = '\u00BD'
# print(num.isnumeric())
# num = '10.5'
# print(num.isnumeric())

# challenge = '30DaysOfPython'
# print(challenge.isidentifier())

# challenge  = 'thirty_days_of_python'
# print(challenge.isidentifier())

# challenge = 'thirty days of python'
# print(challenge.islower())
# challenge = 'Thirty days of python'
# print(challenge.islower())

# challenge = 'thirty days of python'
# print(challenge.isupper())

# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper())

# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = " ".join(web_tech)
# print(result)

# challenge = 'thirty days of pythoonnn'
# print(challenge.strip('noth'))

# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding'))

# challenge = 'thirty days of python'
# print(challenge.split())

# challenge = 'thirty, days, of, python'
# print(challenge.split(', '))

# challenge = 'thirty days of python'
# print(challenge.title())

# challenge = 'thirty days of python'
# print(challenge.swapcase())

# challenge = 'Thirty Days of Python'
# print(challenge.swapcase())

challenge = 'thirty days of Python'
print(challenge.startswith('thirty'))

#case is always sensitive
challenge = 'Thirty days of python'
print(challenge.startswith('thirty'))







