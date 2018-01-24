String = raw_input("Please enter a sentence. NO MISTAKES.")
word = ""
length_word = 0
no_of_words = 0
length_of_string = len(String)
length_of_string_minus_one = length_of_string - 1
index_of_character = 0

for character in String:
	if character == " " or character == "." or index_of_character == length_of_string_minus_one:
		no_of_words += 1
		if len(word) > length_word:
			length_word = len(word)
			
		word = ""
		
	else:
		word += character
	index_of_character += 1

print "number of words %s" % no_of_words
print "length of longest word is %s" % length_word