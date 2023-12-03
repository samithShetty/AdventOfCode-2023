## PART 1
total = 0
with open("input.txt", "r") as infile:
    for line in infile:
        game_id, game = line.strip().split(": ")
        valid = True
        for round in game.split("; "):
            for data in round.split(", "):
                count, color = data.split()
                if color == "red" and int(count) > 12:
                    valid = False
                    break
                if color == "green" and int(count) > 13:
                    valid = False
                    break
                if color == "blue" and int(count) > 14:
                    valid = False
                    break
            if not valid:
                break      
        if valid:
            total += int(game_id.split()[1])
print("Part 1:", total)

### PART 2
total = 0
with open("input.txt", "r") as infile:
    for line in infile:
        game_id, game = line.strip().split(": ")
        max_red = max_green = max_blue = 0 
        for round in game.split("; "):
            for data in round.split(", "):
                count, color = data.split()
                if color == "red" and int(count) > max_red:
                    max_red = int(count)
                if color == "green" and int(count) > max_green:
                    max_green = int(count)
                if color == "blue" and int(count) > max_blue:
                    max_blue = int(count)
        total += max_red * max_green * max_blue
print("Part 2:", total)