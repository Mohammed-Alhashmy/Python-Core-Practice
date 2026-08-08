import timeit
import random


print(timeit.timeit("'Mohammed' * 1"))

print(random.randint(0, 50))


print(timeit.timeit(stmt="random.randint(0, 50)", setup="import random"))
print(timeit.repeat(stmt="random.randint(0, 50)", setup="import random", repeat=5))
