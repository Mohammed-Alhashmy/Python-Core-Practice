import numpy as np 


the_list = [1, 2, 3, 4, 5]

the_array = np.array(the_list)

# print(the_array)
# print(the_list)

# 
# print(type(the_array))

# print(the_array[0])



a = np.array(1)
b = np.array( [5, 10] )
c = np.array( [ [15, 20], [25, 30] ] )
d = np.array( [ [ [35, 40], [45, 50] ],[ [55, 60], [65, 70] ] ] )

print(d[1][0])
print(d[1][0][1])
print(d[1, 0, 1])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



custom_array = np.array([1, 2, 3], ndmin=3)

print(custom_array)
print(custom_array.ndim)

print(custom_array[0, 0, 1]) #bring (2)
