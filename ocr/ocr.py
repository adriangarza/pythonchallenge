#how to find the rarest characters in 2100 lines of random ASCII
inFile = open("input.txt", "r")

#create a dictionary of letter-frequency pairs
chars = {}

for word in inFile:
	for letter in word:
		if letter in chars:
			chars[letter] += 1
		else:
			chars[letter] = 1

#sort the list, then print everything by lowest-highest frequency
for letter in sorted(chars, key=chars.get, reverse=True):
	print(letter, chars[letter])