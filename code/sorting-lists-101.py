# Sorting Lists 101

nums = [3, 5, 4, 2, 1, 1, 1, 1]
sorted_nums_by_value = sorted(nums)
print("Sorted numbers by value", sorted_nums_by_value)
# >>> [1, 1, 1, 1, 2, 3, 4, 5]

names = ["Anna", "Ed", "Abe", "Carol"]
sorted_names_by_alpha_order = sorted(names)
print("Sorted names by alphabetical order", sorted_names_by_alpha_order)
# >>> ["Abe", "Anna", "Carol", "Ed"]

sorted_names_by_len = sorted(names, key=len)
print("Sorted names by name length", sorted_names_by_len)
# >>> ["Ed", "Abe", "Anna", "Carol"]

# sort numbers by high freq to low freq
sorted_nums_by_freq = sorted(nums, key = nums.count, reverse = True)
print("Sorted numbers by frequency", sorted_nums_by_freq)
# >>> [1, 1, 1, 1, 3, 5, 4, 2]
# 3, 5, 4, 2 all appear just once, so they're tied


def list_by_freq(List):
    sorted_List = sorted(List, key=List.count, reverse = True) # same code as above
    final_List = [] # create new list
    for item in sorted_List:
        if item not in final_List:
            final_List.append(item) # avoid adding duplicates
    return final_List
    
print(list_by_freq(nums))
# >>> [1, 3, 5, 4, 2]




