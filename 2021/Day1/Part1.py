# Get the text from the input


with open('2021/Day1/input-advent-1.txt') as f:
    lines = f.readlines()

# Get rid of newlines & convert to numbers

newText = []
for line in lines:
    newLine = int(line.replace('\n', ''))
    newText.append(newLine)

# Iterate through the list and add 1 to the counter when n>n-1

result = 0
for i in range(1, len(newText)):
    if newText[i] > newText[i-1]:
        result +=1

print(result)