### Part 1
# answer = 1
# with open('input.txt', 'r') as infile:
#     times = infile.readline().split()[1:]
#     distances = infile.readline().split()[1:]
#     for i in range(len(times)):
#         # Solve Quadratic Formula
#         b = -int(times[i])
#         c = int(distances[i])
#         temp = ((b ** 2 - 4 * c) ** 0.5)
#         solutions = (-b-temp)/2, (-b+temp)/2
#         if (solutions[0] != int(solutions[0])):
#             answer *= (int(solutions[1]) - int(solutions[0]))
#         else:
#             answer *= (int(solutions[1]) - int(solutions[0]) - 1)
# print(answer)

with open('input.txt', 'r') as infile:
    time = "".join(infile.readline().split()[1:])
    distance = "".join(infile.readline().split()[1:])
    # Solve Quadratic Formula
    b = -int(time)
    c = int(distance)
    temp = ((b ** 2 - 4 * c) ** 0.5)
    solutions = (-b-temp)/2, (-b+temp)/2
    answer = (int(solutions[1]) - int(solutions[0]))
print(answer)