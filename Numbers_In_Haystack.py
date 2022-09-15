# Finds sum of all numbers in a text file.
# Part of the "Python for Everybody" Specialization | https://www.coursera.org/specializations/python
# Sebastian Quirarte | sebastianquirajus@gmail.com

import re

fileh = open("regex_sum_1644489.txt")

values = []
total = 0

for line in fileh:
    nums = re.findall('[0-9]+',line)
    if len(nums) == 0:
        continue
    for i in range(len(nums)):
        values.append(nums[i])

for i in range(len(values)):
    total = total + int(values[i])

print(total)
