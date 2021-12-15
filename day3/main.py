# DAY 3
# Vishal Bakshi

'''
Puzzle 1

Calculate two product of two binary numbers determined from a list of binary numbers:

gamma rate: a binary number made up of the LEAST common bit in each position
epsilon rate: a binary number made up of the LEAST common bit in each position
'''

import os
os.chdir("/Users/vishalbakshi/documents/adventofcode2021/day4")

'''
SOLUTION

read input into a list of strings
Split each string into list or tuple of integers
Loop through and sum the bits in each position
If the sum of bits is more than half the length of input, 1 is the most common bit
If not, 0 is most common bit
Determine the gamma rate and epsilon rate from that
Convert binary numbers to decimal and multiply
'''

def read_input(fname):
    # Read the data into a list
    # Each line becomes a list element
    with open(fname) as f:
        diagnostic_report = f.read().splitlines()

    return diagnostic_report

def calculate_bit_sums(diagnostic_report):
    # Calculate the sum of bits in each position of the binary numbers

    # Initiate 
    bit_sums = [0] * len(diagnostic_report[0])
    for binary_number in diagnostic_report:
        for i in range(len(bit_sums)):
            bit_sums[i] += int(binary_number[i])
    return bit_sums

def get_rates(bit_sums, diagnostic_report_length):
    # The gamma rate is a derived binary number
    # Where each bit is the MOST common bit 
    # in that position in the diagnostic report

    # The epsilon rate is also derived
    # Where each bit is the LEAST common bit 
    # in that position in the diagnostic report
    gamma_rate = ""
    epsilon_rate = ""


    for bit_sum in bit_sums:
        if (bit_sum < diagnostic_report_length / 2):
            gamma_rate += "0"
            epsilon_rate += "1"
        if (bit_sum > diagnostic_report_length / 2):
            gamma_rate += "1"
            epsilon_rate += "0"
    
    return {"gamma_rate": gamma_rate, "epsilon_rate": epsilon_rate}

def binary_to_decimal(binary_number):
    decimal = 0
    for i in range(len(binary_number)):
        power = len(binary_number) - 1 - i
        decimal += int(binary_number[i]) * 2 ** power
    return decimal

def day_three_puzzle_one(fname):
    diagnostic_report = read_input(fname)    
    bit_sums = calculate_bit_sums(diagnostic_report)
    binary_rates = get_rates(bit_sums, len(diagnostic_report))
    decimal_gamma_rate = binary_to_decimal(binary_rates["gamma_rate"])
    decimal_epsilon_rate = binary_to_decimal(binary_rates["epsilon_rate"])
    return decimal_gamma_rate * decimal_epsilon_rate

test_diagnostic_report = read_input("test_input.txt")
test_bit_sums = calculate_bit_sums(test_diagnostic_report)
test_decimal_gamma_rate = binary_to_decimal("10110")
test_decimal_epsilon_rate = binary_to_decimal("01001")

assert test_bit_sums == [7,5,8,7,5]
assert get_rates(test_bit_sums, len(test_diagnostic_report)) == {
    "gamma_rate": "10110", "epsilon_rate": "01001"}
assert test_decimal_gamma_rate == 22
assert test_decimal_epsilon_rate == 9
assert day_three_puzzle_one("test_input.txt") == 198
assert day_three_puzzle_one("input.txt") == 1307354

'''
Puzzle 2

Determine the life support rating which is the product of 
the oxygen generator rating and CO2 scrubber rating.

Oxygen generator rating: the binary number made up of digits MOST common 
in their position

CO2 scrubber rating: the binary number made up of digits LEAST common
in their position
'''

'''
SOLUTION
For each position (index)
    Calculate the most common digit in the list of remaining binary numbers
    Remove binary numbers that don't have that digit in that position
    if one number remains, that's your rating
'''

def get_most_common_digit(bit_sum, number_of_values):
    if bit_sum >= number_of_values / 2:
        return "1"
    else:
        return "0"

def get_least_common_digit(bit_sum, number_of_values):
    if bit_sum < number_of_values / 2:
        return "1"
    else:
        return "0"

def get_rating(diagnostic_report, rating_type, number_of_digits):
    get_common_digit = get_most_common_digit if rating_type ==  "oxygen generator" else get_least_common_digit
    for idx in range(number_of_digits):
        bit_sums = calculate_bit_sums(diagnostic_report)
        most_common_digit = get_common_digit(bit_sums[idx], len(diagnostic_report))
        diagnostic_report = [value for value in diagnostic_report if (value[idx] == most_common_digit)]
        if len(diagnostic_report) == 1: 
            return binary_to_decimal(diagnostic_report[0])
    

def day_three_puzzle_two(fname):
    diagnostic_report = read_input(fname)
    number_of_digits = len(diagnostic_report[0])
    oxygen_generator_rating = get_rating(
        diagnostic_report = diagnostic_report, 
        rating_type = "oxygen generator", 
        number_of_digits = number_of_digits)

    co2_scrubber_rating = get_rating(
        diagnostic_report = diagnostic_report, 
        rating_type = "co2 scrubber", 
        number_of_digits = number_of_digits)
    
    return oxygen_generator_rating * co2_scrubber_rating

assert get_least_common_digit(test_bit_sums[0], 5) == "0"
assert get_most_common_digit(test_bit_sums[0], 5) == "1"
assert get_rating(test_diagnostic_report, "oxygen generator", 5) == 23
assert get_rating(test_diagnostic_report, "co2 scrubber", 5) == 10
assert day_three_puzzle_two("test_input.txt") == 230
assert day_three_puzzle_two("input.txt") == 482500
