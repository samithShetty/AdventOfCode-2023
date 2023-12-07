## Part 1
# answer = 0
# def hand_to_score(hand:str):
#     counts = []
#     while hand:
#         counts.append(int(hand.count(hand[0])))
#         hand = hand.replace(hand[0], "")
#     counts = sorted(counts, reverse=True)
#     return counts[0] * 10 + (counts[1] if len(counts) > 1 else 0)
# with open('input.txt', 'r') as infile:
#     hands_bucket = dict()
#     lines = infile.readlines()
#     for line in lines:
#         hand, bet = line.split()
#         score = hand_to_score(hand)
#         hands_bucket[score] = hands_bucket.get(score, list())
#         hands_bucket[score].append((hand, int(bet)))
#     print(hands_bucket)
#     rank = len(lines)
#     for score in sorted(hands_bucket.keys(), reverse=True):
#         for hand, bet in sorted(hands_bucket[score], key=lambda x:["AKQJT987654321".index(c) for c in x[0]]):
#             answer += bet * rank
#             print(hand, bet, rank)
#             rank -=1
# print(answer)

### Part 2
answer = 0
def hand_to_score(hand:str):
    counts = []
    joker_count = hand.count("J")
    hand = hand.replace("J", "")
    while hand:
        counts.append(int(hand.count(hand[0])))
        hand = hand.replace(hand[0], "")
    counts = sorted(counts, reverse=True)
    return (((counts[0] + joker_count) if len(counts) > 0 else 5) * 10) + (counts[1] if len(counts) > 1 else 0)

with open('input.txt', 'r') as infile:
    hands_bucket = dict()
    lines = infile.readlines()
    for line in lines:
        hand, bet = line.split()
        score = hand_to_score(hand)
        hands_bucket[score] = hands_bucket.get(score, list())
        hands_bucket[score].append((hand, int(bet)))
    print(hands_bucket)
    rank = len(lines)
    for score in sorted(hands_bucket.keys(), reverse=True):
        for hand, bet in sorted(hands_bucket[score], key=lambda x:["AKQT98765432J".index(c) for c in x[0]]):
            answer += bet * rank
            print(score, hand, rank)
            rank -=1
print(answer)