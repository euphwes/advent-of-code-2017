
with open('day_1.txt', 'r') as f:
	day_1_input = f.read()

matching_digits = list()
matching_part_2 = list()

start_i = 0
length = len(day_1_input)

for i in range(0, len(day_1_input)):
	j = (i+1) % len(day_1_input)
	if day_1_input[i] == day_1_input[j]:
		matching_digits.append(int(day_1_input[i]))


print(sum(matching_digits))
print("")

for i in range(0, len(day_1_input)):
	j = int((i+len(day_1_input)/2) % len(day_1_input))
	if day_1_input[i] == day_1_input[j]:
		matching_part_2.append(int(day_1_input[i]))

print(sum(matching_part_2))
