test_tuple = (6, 7, 8, 6, 7, 10)

# Printing original tuple
print("The original tuple : " + str(test_tuple))

# Maximum frequency in Tuple
# Using loop + count()
cnt = 0
res = test_tuple[0]

for ele in test_tuple:
	curr_freq = test_tuple.count(ele)

	if(curr_freq > cnt):
		cnt = curr_freq
		res = ele

print("Maximum element frequency tuple : " + str(res))
