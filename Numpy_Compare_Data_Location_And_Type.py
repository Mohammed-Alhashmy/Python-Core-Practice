import numpy as np


the_list = [1, 2, 3, 4, 5]
the_array = np.array([1, 2, 3, 4, 5])


print(the_list[0])
print(the_list[1])


print(the_array[0])
print(the_array[1])


print(id(the_list[0]))
print(id(the_array[0]))




data_list = [1, 2, 3, "a", True, False, 25.5]
data_array = np.array([1, 2, 3, "a", True, False, 25.5])

print(type(data_list[1]))
print(type(data_array[1]))


data_list_two = [1, 2, 3, "a", True, False, 25.5]
data_arraytwo = np.array([1, 2, 3, 30.5])

print(type(data_list_two[1]))
print(type(data_arraytwo[1]))