# Get the text from the input


with open('2021/Day1/input-advent-1.txt') as f:
    input_lines = f.readlines()

# Get rid of newlines & convert to numbers

depths_list = []
for line in input_lines:
    depth_num = int(line.replace('\n', ''))
    depths_list.append(depth_num)

# Iterate through the list and add 1 to the counter when the sliding window sum is greater than the previous one

num_window_greater_than_previous = 0
for i in range(1, len(depths_list)-2):
    if (depths_list[i]+depths_list[i+1]+depths_list[i+2]) > (depths_list[i-1]+depths_list[i]+depths_list[i+1]):
        num_window_greater_than_previous +=1

print(num_window_greater_than_previous)