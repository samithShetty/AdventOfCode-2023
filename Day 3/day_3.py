### PART 1
def check_left(col, row_text):
    num_str = ""
    while col >= 0 and row_text[col].isdigit():
        num_str = row_text[col] + num_str
        col -= 1
    return num_str

def check_right(col, row_text):
    num_str = ""
    while col < len(row_text) and row_text[col].isdigit():
        num_str += row_text[col]
        col += 1    
    return num_str

def check_vert(col, row_text):
    left = check_left(col-1, row_text)
    right = check_right(col + 1, row_text)

    # Number in middle
    if row_text[col].isdigit():
        return (left + row_text[col] + right,)
    # No Number in middle (Check corners)
    else:
        return (left, right)

total = 0
with open('input.txt', 'r') as infile:
    input_text = infile.readlines()
    for row in range(len(input_text)):
        for col in range(len(input_text[row])):
            adj_nums = []
            # Check if char is Symbol
            if not input_text[row][col].isdigit() and input_text[row][col] not in [".", "\n"]:
                adj_nums.append(check_left(col - 1, input_text[row]))
                adj_nums.append(check_right(col + 1, input_text[row]))
                if row > 0:
                    adj_nums.extend(check_vert(col, input_text[row -1]))      
                if row < len(input_text) - 1:
                    adj_nums.extend(check_vert(col, input_text[row +1]))
            for num in adj_nums:
                if num:
                    total += int(num)
print(total)

### PART 2
def check_left(col, row_text):
    num_str = ""
    while col >= 0 and row_text[col].isdigit():
        num_str = row_text[col] + num_str
        col -= 1
    return num_str

def check_right(col, row_text):
    num_str = ""
    while col < len(row_text) and row_text[col].isdigit():
        num_str += row_text[col]
        col += 1    
    return num_str

def check_vert(col, row_text):
    left = check_left(col-1, row_text)
    right = check_right(col + 1, row_text)

    # Number in middle
    if row_text[col].isdigit():
        return (left + row_text[col] + right,)
    # No Number in middle (Check corners)
    else:
        return (left, right)

total = 0
with open('input.txt', 'r') as infile:
    input_text = infile.readlines()
    for row in range(len(input_text)):
        for col in range(len(input_text[row])):
            adj_nums = []
            # Check if char is Symbol
            if input_text[row][col] == "*":
                adj_nums.append(check_left(col - 1, input_text[row]))
                adj_nums.append(check_right(col + 1, input_text[row]))
                if row > 0:
                    adj_nums.extend(check_vert(col, input_text[row -1]))      
                if row < len(input_text) - 1:
                    adj_nums.extend(check_vert(col, input_text[row +1]))
            
            adj_nums = [num for num in adj_nums if num] # Clear empty num strings
            if len(adj_nums) == 2:
                total += int(adj_nums[0]) * int(adj_nums[1])
print(total)