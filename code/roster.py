# opening the class roster to read
file = open("class-roster-majors-years.csv", "r")

# take in data
data = file.read().split("\n")

# print(data)

del data[0] # deletes header row
# print(data)


# print(data[0]) # print first student row

student = data[0].split(",")
# print(student)
first_name = student[1].strip('"') # remove quotation mark
last_name = student[0].strip('"')
full_name = first_name + " " + last_name
# print(full_name)

names = []
schools = []
years = []

for i in range(len(data)):
    student = data[i].split(",") # ['Zhao"', '"Emily', 'Tisch', 'Super Senior']
    first_name = student[1].strip('"') # "Emily -> Emily
    last_name = student[0].strip('"') # Zhao" -> Zhao
    full_name = first_name + " " + last_name # Emily Zhao
    names.append(full_name) # add student full name
    schools.append(student[2]) # add school
    years.append(student[3]) # add year

# print(names)
# print(schools)
# print(years)

# Function that I wrote
def most_common(List): # return most common value
    # create a count variable to hold the highest count so far
    # create another variable to hold the value of the highest count
    count = 0
    item_value = List[0] # initialize as first list value

    # go through every item in the list
    # count how many times the item is in the list
    # if that count is greater than count variable, update it
    # update the item value
    for item in List:
        if List.count(item) > count:
            count = List.count(item)
            item_value = item
    return item_value
 

# Function I got from the internet 
def most_frequent(List):
    return max(set(List), key = List.count)

print("Most common year:", most_common(years))
print("Most common school:", most_common(schools))
# print(most_frequent(years)) # it returns the same thing!

def list_by_freq(List): # refer to SortingLists101.py
    sorted_List = sorted(List, key=List.count, reverse = True) # same code as above
    final_List = [] # create new list
    for item in sorted_List:
        if item not in final_List:
            final_List.append(item) # avoid adding duplicates
    return final_List

print("List of schools from most to least common", list_by_freq(schools))
                                                              
roster = {}
# create a roster of keys (student names) and values (their years)
for i in range(len(names)):
    roster[names[i]] = years[i]
#print(roster)


'''
# print names
for name in roster.keys():
    print(name)

# print years
for year in roster.values():
    print(year)

# print name + year
for name, year in roster.items():
    print(name, year)

'''

print("List of years from most to least common", list_by_freq(list(roster.values())))


# creating a file of my findings
file2 = open('class-info-for-bossman.txt', 'w')

file2.write("List of all my students: \n")
for name in names:
    file2.write(name + "\n")
file2.write("\n")

file2.write("Most popular majors: \n")
for school in listByFreq(schools):
    file2.write(school + "\n")
file2.write("\n")

file2.write("Most popular years: \n")
for year in listByFreq(years):
    file2.write(year + "\n")
file2.close()
      

    
