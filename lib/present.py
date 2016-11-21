import time

import file, ipa, format

words = file.load('words')
word_pronunciations = file.load('word_pronunciations')

def present_word(word, existing_word):
	if existing_word:
		return '{} (word exists already: {})'.format(word, existing_word)
	else:
		return word

def already_in_dictionary(word):
	if word in word_pronunciations:
		index = word_pronunciations.index(word)
		return words[index]

def present(word):
	existing_word = already_in_dictionary(word)
	print present_word(word, existing_word)
	time.sleep(0.2)

def present_for_web(word):
	ipa_word = ipa.ipa(word[1:])
	
	formatted_word = format.format(word)
	existing_word = already_in_dictionary(formatted_word)
	
	return present_word(ipa_word, existing_word)