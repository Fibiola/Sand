# this is where user puts in a word that gets stored in the variable called original.
original = raw_input("Give me an English word to translate to Pig Latin")

# we want to make sure user inputted SOMETHING. Therefore we check the length. 
# we also make sure its a word. Not number.
pig = "way"
pyg = "ay"
word = original.lower()
first = word[0]
new_word = word + pig
not_vowel = word[1:] + first + pyg
if len(original) > 0 and original.isalpha():
	if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
		print new_word
	else:
		print not_vowel
else:
	print "Empty"



