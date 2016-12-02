# Uncann.ly

Get the most phonetically probable yet missing words in the English language.

Visit [http://uncannly.cfapps.io](http://uncannly.cfapps.io) for a demonstration.

## Endpoints:

/random_word

/words
Query params:
* style: sorted, random
* filter: continued_product, averaging
* weighted_by_frequency: true/false
* include_real_words: true/false
* return_count: int < several thousand or so I guess

i.e.
words?style=sorted&filter=continued_product&weighted_by_frequency=true&include_real_words=true&return_count=4

## Terminal scripts:

bin/random_probable_words

bin/most_probable_words
Flags:
* -u --unweighted 
* -x --exclude-real-words  (STILL HAVENT DONE THIS ONE YET)
* -a --by-averaging            
* -c --by-continued-product   
* -s --sorted
* -r --random