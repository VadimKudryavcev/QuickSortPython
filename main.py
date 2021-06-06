import time
from quicksort import *

array = [10, 16, 8, 8, 12, 15, 6, 3, 9, 5]

time0 = time.time()
quicksort(array, 0, len(array) - 1)
time1 = time.time()

print('Sorted')
print(array)

print('Время расчета {} секунд'.format(time1 - time0))