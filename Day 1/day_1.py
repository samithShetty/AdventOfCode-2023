### PART 1
# with open("input.txt", 'r') as infile:
#     total = 0
#     for line in infile:
#         print(line)
#         for char in line:
#             if char.isdigit():
#                 total += 10 * int(char)
#                 print(int(char))
#                 break
            
        
#         for char in line[::-1]:
#             if char.isdigit():
#                 total += int(char)
#                 print(int(char))
#                 break
    
#     print(total)


def str_to_num(string, backwards = False):
    length = len(string)
    if length >= 3:
        match_str = string[:3] if backwards else string[-3:] 
        match match_str:
            case "one":
                return 1
            case "two":
                return 2
            case "six":
                return 6
    if length >= 4:        
        match_str = string[:4] if backwards else string[-4:] 
        match match_str:
            case "four":
                return 4
            case "five":
                return 5
            case "nine":
                return 9
    if length >= 5:
        match_str = string[:5] if backwards else string[-5:] 
        match match_str:
            case "three":
                return 3
            case "seven":
                return 7
            case "eight":
                return 8
    return 0


with open("input.txt", 'r') as infile:
    total = 0
    for line in infile:
        word= ""
        for char in line:
            if char.isdigit():
                total += 10 * int(char)
                break
            else:
                word += char
                word_val = str_to_num(word)
                if word_val != 0:
                    total += 10 * word_val
                    break

        word = ""
        for char in line[::-1]:
            if char.isdigit():
                total += int(char)
                break
            else:
                word = char + word
                print(word)
                word_val = str_to_num(word, True)
                if word_val != 0:
                    total += word_val
                    break
    print(total)