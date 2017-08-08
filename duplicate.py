'''
Write a program that accepts a sequence of whitespace separated words 
as input and prints the words after removing all duplicate words and 
sorting them alphanumerically. Suppose the following input is 
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()


# Define this function to return the expected output
# Do not print it from this function
def singlify(str):
	# TODO
	output = []
	duplicate = []

	output_word = ''

	for word in str:
		new_word = word.lower() 
		if new_word not in duplicate: 
			duplicate.append(new_word) 
			output.append(word)
			output.sort()
	

	

	

print(singlify(sentence.split(" ")))
