# Daily Challenge:

# Creating nested list with the code inside
neos_code = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

# creating two global variables for conditions
symbols = ['#', '@', '$', '%', '^', '!']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# function to check each row


def code_solution(code):
    # empty string to concatenate inside only letters from the first column
    answer_first_column = ""
    # creating a list with only first column items
    first_column = [item[0] for item in code]
    # three conditions to check
    # 1.if the letter is a-z and if yes add it to the empty string
    # 2.if the item is in the symbol list than make a space instead of the symbol
    # 3. if the item is a number instead of number close the space
    for i in first_column:
        if i.isalpha():
            answer_first_column += i
        elif i in symbols:
            answer_first_column += " "
        elif i in nums:
            answer_first_column += ""

    answer_second_column = ""
    second_column = [item[1] for item in code]
    for j in second_column:
        if j.isalpha():
            answer_second_column += j
        elif j in symbols:
            answer_second_column += " "
        elif j in nums:
            answer_second_column += ""

    answer_third_column = ""
    third_column = [item[2] for item in code]
    for k in third_column:
        if k.isalpha():
            answer_third_column += k
        elif k in symbols:
            answer_third_column += " "
        elif k in symbols:
            answer_third_column += ""

    # Printing the result from the three strings that have been created out of the three columns.
    print(answer_first_column + answer_second_column + answer_third_column)


code_solution(neos_code)
