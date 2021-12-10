# Get the input data

with open("2021/Day4/input-day-4.txt") as f:
    input_lines = f.readlines()

# Clean the data

bingo_nums = input_lines[0].replace("\n", "").split(',')
bingo_cards = input_lines[2::]
bingo_cards_clean = []
for i in range(0, len(bingo_cards)):
    if bingo_cards[i] == '\n':
        pass
    else:
        bingo_cards_clean.append(bingo_cards[i].replace('\n', ''))
bingo_cards = bingo_cards_clean


bingo_cards_clean = []
for i in range(0, len(bingo_cards),5):
    bingo_cards_clean.append(bingo_cards[i:i+5])
bingo_cards = bingo_cards_clean
    

bingo_cards_clean = []
for bingo_card in bingo_cards:
    card = []
    for string in bingo_card:
        line = []
        numList = string.split(' ')
        for num in numList:
            if num == '':
                pass
            else:
                line.append(int(num))
        card.append(line)
    bingo_cards_clean.append(card)

bingo_cards = bingo_cards_clean
        
#   Get the winning card




def validate_bingo(nums, cards):
#     iterate through the numbers and mark the called number
    for num in nums:
        for card in cards:
            for line in card:
                for i in range(0,5):
                    if line[i] == int(num):
                        line[i] = 'X'
#     look for a winner
        for card in cards:
            for line in card:
                if line[0] == line[1] == line[2] == line[3] == line[4]:
                    
                    return [card, num]
            for i in range(0,5):
                if card[0][i] == card[1][i] == card[2][i] == card[3][i] == card[4][i]:
                    return [card, num]
                


def calculate_score(card):
    number = int(card[1])
    score =0
    for line in card[0]:
        for element in line:
            if type(element) == int:
                score+=element
    print(score*number)


calculate_score(validate_bingo(bingo_nums, bingo_cards))