# DAY 4
# Vishal Bakshi

'''
Puzzle 1

Find out which bingo board will win (most points when reaching bingo)
'''

import os
os.chdir("/Users/vishalbakshi/documents/adventofcode2021/day4")

'''
SOLUTION
Read the data into lists
Create helper function to scan the bingo board for a win 
given the randomly drawn number and return the point sum
Pick the board with the highest point sum
'''
def read_input(fname):
    '''
    Read the input txt file into lists
    The first list is the ordered numbers drawn
    The second list is a 3-level nested list of bingo boards where
        level 1 contains all bingo boards
        level 2 contains one bingo board
        level 3 contains one row of a bingo board
    Each bingo board row has 5 integers
    Each bingo board has 5 rows
    '''
    with open(fname) as f:
        board_row_count = 0
        bingo_boards = []
        board_rows = []
        lines = f.readlines()
        for line in lines:
            if line != "\n":
                line = line.strip()
                line = line.split(" ")

                # Capture the list of randomly drawn numbers
                if len(line) == 1:
                    randomly_drawn_numbers = line[0].split(",")
                    randomly_drawn_numbers = [int(number) for number in randomly_drawn_numbers]

                # Capture bingo boards
                if len(line) > 1:
                    board_row_count += 1

                    # Filter out empty strings
                    line = [int(number) for number in line if number != ""]

                    #Append board row to list of board rows
                    board_rows += [line]

            # Each board has 5 rows so you have reached the end of
            # a board when the counter is at 5
            if board_row_count == 5:
                bingo_boards += [board_rows]

                # Prep the list/counter for the next board
                board_rows = [] 
                board_row_count = 0

    return {"randomly_drawn_numbers": randomly_drawn_numbers, "bingo_boards": bingo_boards}

def calculate_score(unmarked_sum, last_drawn_number):
    return unmarked_sum * last_drawn_number

def get_unmarked_sum(board):
    return sum(sum(x) if isinstance(x, list) else x for x in board)

def check_columns(board, drawn_numbers):
    bingo = False
    # Loop through each column
    for col_idx in range(len(board[0])):
        marked_numbers = 0
        for row_idx in range(len(board)):
            # Capture the value at the given column and row index
            value = board[row_idx][col_idx]

            # If the value matches the drawn number increment counter
            if value in drawn_numbers:
                marked_numbers += 1

                # "mark" the number as 0
                # so that later the unmarked_sum can be calculated
                board[row_idx][col_idx] = 0
        # bingo!
        if marked_numbers == len(board[row_idx]):
            bingo = True

    unmarked_sum = get_unmarked_sum(board)
    score = calculate_score(unmarked_sum, drawn_numbers[-1])
    return {"result": bingo, "score": score}

def check_rows(board, drawn_numbers):
    bingo = False
    for row in board:
        marked_numbers = 0
        for i, value in enumerate(row):
             # If the value matches the drawn number, increment the counter
            if value in drawn_numbers:
                marked_numbers += 1

                # "mark" the number as 0
                # so that later the unmarked_sum can be calculated
                row[i] = 0
        # bingo!
        if marked_numbers == len(row):
            bingo = True
    
    unmarked_sum = get_unmarked_sum(board)
    score = calculate_score(unmarked_sum, drawn_numbers[-1])
    return {"result": bingo, "score": score}

def is_bingo(board, drawn_numbers, i):
    is_column_bingo = check_columns(board, drawn_numbers[:i])
    is_row_bingo = check_rows(board, drawn_numbers[:i])

    # Return whichever gets a bingo first (columns or rows)
    if is_column_bingo["result"]:
        return is_column_bingo
    elif is_row_bingo["result"]:
        return is_row_bingo
    
    # No bingo found
    else:
        return {"result": False}

def get_scores(bingo_boards, drawn_numbers):
    # Prepare scores list to track when a board has a bingo
    scores = [None] * len(bingo_boards)

    # Check each board
    for board_idx, board in enumerate(bingo_boards):
        # incremental randomly drawn numbers
        for drawn_idx in range(1, len(drawn_numbers)):
            # check if board has a bingo
            bingo = is_bingo(board, drawn_numbers, drawn_idx)

            # if board has bingo
            # store the FIRST drawn number when it got the bingo
            # as well as the score
            if bingo["result"]:
                if scores[board_idx] == None:
                    scores[board_idx] = [drawn_idx, bingo["score"]]
    # Scores is a nested list
    # For the three test input boards: [[12, 4512], [14, 2192], [15, 1924]]
    return scores


def day_four(fname, puzzle="one"):
    # Read in the data
    input = read_input(fname)
    randomly_drawn_numbers = input["randomly_drawn_numbers"]
    bingo_boards = input["bingo_boards"]  

    # Calculate the scores for each winning board

    scores = get_scores(bingo_boards, randomly_drawn_numbers)

    # Sort the list by randomly drawn number index
    scores.sort()

    if puzzle == "one":
        # return the first score
        return scores[0][1]
    elif puzzle == "two":
        #return last score
        return scores[-1][1]
    else:
        return None

test_input = read_input("test_input.txt")
test_randomly_drawn_numbers = test_input["randomly_drawn_numbers"]
test_bingo_boards = test_input["bingo_boards"]

assert test_randomly_drawn_numbers == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
assert test_bingo_boards == [
    [
        [22, 13, 17, 11, 0], 
        [8, 2, 23, 4, 24], 
        [21, 9, 14, 16, 7], 
        [6, 10, 3, 18, 5], 
        [1, 12, 20, 15, 19]], 
    [
        [3, 15, 0, 2, 22], 
        [9, 18, 13, 17, 5], 
        [19, 8, 7, 25, 23], 
        [20, 11, 10, 24, 4], 
        [14, 21, 16, 12, 6]], 
    [
        [14, 21, 17, 24, 4], 
        [10, 16, 15, 9, 19], 
        [18, 8, 23, 26, 20], 
        [22, 11, 13, 6, 5], 
        [2, 0, 12, 3, 7]]]

assert check_rows(test_bingo_boards[2], test_randomly_drawn_numbers[:12]) == {'result': True, 'score': 4512}
assert is_bingo(test_bingo_boards[2], test_randomly_drawn_numbers, 12) == {'result': True, 'score': 4512}
assert check_columns(test_bingo_boards[1], test_randomly_drawn_numbers[:15]) == {'result': True, 'score': 1924}
assert is_bingo(test_bingo_boards[1], test_randomly_drawn_numbers, 15) == {'result': True, 'score': 1924}
assert day_four("test_input.txt", puzzle="one") == 4512
assert day_four("test_input.txt", puzzle="two") == 1924