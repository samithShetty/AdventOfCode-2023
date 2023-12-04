### Part 1
total = 0
with open('input.txt', 'r') as infile:
    for line in infile:
        card_total = 0
        win_nums, my_nums = line.split("|")
        win_nums = win_nums.split()[2:]
        my_nums = my_nums.split()
        for num in my_nums:
            if num in win_nums:
                card_total += 1 if card_total == 0 else card_total
        total += card_total
print(total)

### Part 2
with open('input.txt', 'r') as infile:
    total = 0
    lines = infile.readlines()
    copies = {i: 1 for i in range(len(lines))}
    for index, line in enumerate(lines):
        total += copies[index]
        matches = 0
        win_nums, my_nums = line.split("|")
        win_nums = win_nums.split()[2:]
        my_nums = my_nums.split()
        for num in my_nums:
            if num in win_nums:
                matches += 1
        for i in range(1, matches+1):
            copies[i + index] += copies[index]
    print(total)
