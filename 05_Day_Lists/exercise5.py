#ex1
empty_list = []
#ex2
another_list = [0,1,2,3,4,5]
#ex3
length = len(another_list)

#ex4
print(another_list[0])
print(another_list[2:4]) #middle item of list, took 2 numbers cuz list len is even
print(another_list[-1]) #last item

#ex5
mixed_data_types = ['Angelina Jolie', 34, 173.2, 'Divorced', {'country':'USA', 'city':'NY'}]
print(mixed_data_types)

#ex6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#ex7
print(it_companies)

#ex8
num_companies = len(it_companies)

#ex9
middle_company = int((num_companies - 1) / 2) #assuming odd size list
print(it_companies[0]) #lists will always start at 0 no matter what
print(it_companies[middle_company])
print(it_companies[-1]) #this will always return the last element no matter what

#ex10
it_companies[3] = 'Nvidia'
print(it_companies)

#ex11
it_companies.append('DELL')
print(it_companies)

#ex12
it_companies[middle_company] = 'Cisco' # it inserted in the middle but the list is even so unbalanced
print(it_companies)

#ex13
it_companies[2] = it_companies[2].upper()
print(it_companies)

#ex14
companies = '#; '.join(it_companies)
print(companies)

#ex15
does_exit = 'DELL' in it_companies
if does_exit:       #suggested to not write `if does_exist == True`
    print(f"the company exists")
else:
    print(f"does not exist")

#ex16
it_companies.sort()
print(it_companies)

#ex17
it_companies.sort(reverse=True)
print(it_companies)

#ex18
it_companies = it_companies[3:] #slice first 3 companies
print(it_companies)

#ex19
it_companies = it_companies[:-3] #slice last 3 companies
print(it_companies)

#ex20
# middle_company = int((len(it_companies) - 1) / 2)
# print(len(it_companies))
# print(middle_company)

# #the list at this stage is ['Google', 'Facebook'], I cannot get this to work
# if len(it_companies) % 2 == 0: #cuz its even
#     it_companies = it_companies[0:2]
#     print('even length')
# elif (len(it_companies) % 2 == 0) and len(it_companies) == 2:
#     it_companies = it_companies[0:middle_company]
# else:
#     it_companies = it_companies.pop(middle_company)
#     print('odd length')
# print(it_companies)

#ex20 - working!
def delete_middle(it_companies):
    '''
    Computes the index for the middle company and deletes it
    handles odd, even or small length lists. Does not handle 1 or 0 len lists
    '''
    middle_company = int((len(it_companies) - 1) / 2)
    # print(len(it_companies))
    # print(middle_company)

    if len(it_companies) == 2:
        del it_companies[0:2]
        print("list is small so, 2")

    elif len(it_companies) % 2 == 0:
        del it_companies[middle_company:middle_company+2]
        print('list is even is modular')
    else:
        del it_companies[middle_company]
        print('list is odd')

delete_middle(it_companies)
print(it_companies)


#ex21
more_companies = ['Nvidia', 'Cisco', 'DELL']
it_companies.extend(more_companies)
print(it_companies)
del it_companies[0]
print(it_companies)
# it_companies = it_companies.pop(0)
# print(type(it_companies))
# print(it_companies)

#ex22
# it_companies = it_companies.pop(middle_company)
# print(it_companies)
delete_middle(it_companies)
print(it_companies)

#ex23
it_companies.extend(more_companies)
del it_companies[-1]
print(it_companies)

#ex24
it_companies.clear()
print(it_companies)

#ex25
del it_companies

#ex26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
new_list = front_end + back_end
print(new_list)

#ex27
full_stack = new_list.copy()
pointer = full_stack.index('Redux') + 1 #insert after
full_stack.insert(pointer, 'Python')
print(full_stack)
full_stack.insert((pointer+1),'SQL')
print(full_stack)


#ex2.1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25,24]
ages.sort()  #assuming we do not use .min() or .max()
min = ages[0] #minimum age cuz first element sorted in ascending
max = ages[-1] #maximum age cus last element
print(f"Min age = {min}, max age = {max}")

#ex2.2 
min_max = [min, max]
ages.extend(min_max)
print(ages)

#ex2.3
ages.sort()
length = len(ages)
print(ages)

#ex2.4
if length % 2 == 0:
    print("length is even, computing 2 values")
    middle_index = int((length - 1) /2)
    median_age = (ages[middle_index] + ages[middle_index+1]) / 2
    print(f"Median age = {median_age}")
else:
    print("length is odd, computing 2 values")
    middle_index = int((length - 1)/2)
    median_age = (ages[middle_index])
    print(f"Median age = {median_age}")

#ex2.5
age_sum = 0
for i in range(length):
    age_sum += ages[i]
avg_age = int((age_sum / length)) #will give 22.75 but we are dealing with whole values for age so cast
print(f"Average age = {avg_age}")

#ex2.6
range = max - min
print(f"Range of ages = {range}")

#ex2.7
if abs(min - avg_age) < (max - avg_age):
    print("min - average is less")
elif abs(min - avg_age) > (max - avg_age):
    print("min - average is greater")
else:
    print("neither")

#ex2.8 +ex2.9
from countries import countries
country_list = countries.copy() #obtain a copy dont edit it raw!

def find_middle(country_list):
    middle_country = int((len(country_list) - 1) / 2)
    # print(len(country_list))
    # print(middle_country)

    if len(country_list) % 2 == 0:
        print(country_list[middle_country], country_list[middle_country+1])
        print('list is even is modular')
        list1 = country_list[:(middle_country+1)]
        list2 = country_list[(middle_country+1):]
        print(list1, list2)
    else:
        print(country_list[middle_country])
        print('list is odd')
        list1 = country_list[:(middle_country+1)]
        list2 = country_list[(middle_country+1):]
        print(list1)
        print(list2)
find_middle(country_list)

#ex2.30
mini_country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, us, *scandic = mini_country_list
print(china, russia, us, scandic)


