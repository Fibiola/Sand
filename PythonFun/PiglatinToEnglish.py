original = raw_input("Give me a pig latin word to translate to English ")

#Pig defined word for words starting with vowel
#Pyg defined word for words starting with not_vowel.
pig = "way"
pyg = "ay"
word = original.lower()
removedAY = word[:-2]
removedWAY = word[:-3]
first = word[1]
new_word = removedAY[-1] + removedAY[:-1] 

if len(word) > 0 and original.isalpha():
	if first == "a" or first =="e" or first == "i" or first == "o" or first == "u" 
		print new_word
	else 
print new_word
else print "not a word"

# we dont know if it was a word that previously contained a wovel or not. 