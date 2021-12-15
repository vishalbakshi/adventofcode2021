# DAY 1
# Vishal Bakshi
'''
Puzzle #1
Objective: count the number of times a depth measurement increases from the previous measurement. 
There is no measurement before the first measurement.

Lesson learned: don't forget to convert str to int before comparing values
'''
import os
os.chdir("/Users/vishalbakshi/documents/adventofcode2021/day4")

# Load the txt file into a list
# Strip the new line character
# Convert all elements from str to int
with open('input.txt') as f:
    measurements = f.read().splitlines()

measurements = [int(i) for i in measurements]
'''
SOLUTION 1

Loop through the list and compare each value to the previous
If the value is larger, increment the counter
Set current value as `previous_value` at the end of the loop
'''

def day_one_puzzle_one(measurements):
    count_measurement_increase = 0
    previous_value = measurements[0]
    for value in measurements:
        if value > previous_value:
            count_measurement_increase += 1
        previous_value = value
    return count_measurement_increase

test_measurements = [199,200,208,210,200,207,240,269,260,263]
assert day_one_puzzle_one(test_measurements) == 7
assert day_one_puzzle_one(measurements) == 1446

'''
Puzzle #2
Objective: count the number of times the sum of sliding window increases from the previous sum. 
There is no measurement before the first measurement.
'''


'''
SOLUTION 1

Start with the sum of the first three measurements
Loop through the measurements
Convert str to int
Subtract the first value from sum
Add the current value to the previous two
Compare the sums
'''
def day_one_puzzle_two(measurements):
    previous_sum = sum(measurements[0:3])
    count_sum_increase = 0
    
    for i in range(len(measurements) - 2):
        current_sum = sum(measurements[i:i+3])
        if (current_sum > previous_sum):
            count_sum_increase += 1
        previous_sum = current_sum
    return count_sum_increase

test_measurements = [199,200,208,210,200,207,240,269,260,263]
assert day_one_puzzle_two(test_measurements) == 5
assert day_one_puzzle_two(measurements) == 1486