import sys

from ipa import ipa
from type_conversion import array_to_string
from data.load_data import load_words

dictionary = load_words(unstressed=False)
dictionary_unstressed = load_words(unstressed=True)

class Present:
	@staticmethod
	def for_web(word, unstressed, exclude_real):
		ipa_word = ipa(word)
		
		stringified_word = array_to_string(word)
		existing_word = already_in_dictionary(stringified_word, unstressed)
		
		return present_word(ipa_word, exclude_real, existing_word)

	@staticmethod
	def for_terminal(word, unstressed, exclude_real, suppress_immediate):
		existing_word = already_in_dictionary(word, unstressed)
		word = present_word(word, exclude_real, existing_word)
		if word == False:
			return False
		else:
			if not suppress_immediate:
				sys.stdout.write(word + '\n')
			return word

def present_word(word, exclude_real, existing_word):
	if existing_word:
		return False if exclude_real else '{} ({})'.format(word, existing_word)
	else:
		return word

def already_in_dictionary(word, unstressed):
	words = dictionary_unstressed if unstressed else dictionary
	for (spelling, pronunciation) in words:
		if word == pronunciation:
			return spelling
