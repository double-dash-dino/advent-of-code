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