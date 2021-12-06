# DAY 2
# Vishal Bakshi
'''
Puzzle #1
Objective: find the product of the submarine's final horizontal position and depth
after it follows the planned course in the input file with 
`forward` (changing horizontal position) and `up`/`down` (changing depth)

`up` decreases depth
`down` increases depth

Lessons learned: Create a .txt with test input (instead of a list) in order to test the 
read functionality
'''

import os
os.chdir("/Users/vishalbakshi/documents/adventofcode/day2")

'''
SOLUTION (~15 minutes)

read input file and split each line into a tuple (direction, units)
loop through the list of tuples
if the direction is forward, add the units to the horizontal position
if the direction is up, subtract the units from depth
if the direction is down, add the units to depth
return the product of horizontal position and depth
'''
def read_input_file(fname):
    # Read the data into a list
    # Each line becomes a list element
    with open(fname) as f:
        course = f.read().splitlines()

    # Split each element (e.g. "forward 1") into a list ['forward', '1']
    course = [s.split(' ') for s in course]

    # Convert units to int
    course = [(s[0], int(s[1])) for s in course]

    return course

def day_two_puzzle_one(fname):
    course = read_input_file(fname)

    # Initialize positions
    horizontal_position = 0
    depth = 0

    for direction, units in course:
        if (direction == "forward"): 
            horizontal_position += units
        if (direction == "up"):
            depth -= units
        if (direction == "down"):
            depth += units

    return horizontal_position * depth

assert day_two_puzzle_one("test_input.txt") == 150
assert day_two_puzzle_one("input.txt") == 1561344

'''
Puzzle 2

this introduces an `aim` command in the course 
`aim` is multiplied by forward to determine the change in depth

'''

def day_two_puzzle_two(fname):
    course = read_input_file(fname)

    # Initialize positions
    horizontal_position = 0
    depth = 0
    aim = 0

    for direction, units in course:
        if (direction == "forward"):
            horizontal_position += units
            depth = depth + units * aim
        if (direction == "down"): 
            aim += units
        if (direction == "up"):
            aim -= units
    
    return horizontal_position * depth

assert day_two_puzzle_two("test_input.txt") == 900

print(day_two_puzzle_two("input.txt"))