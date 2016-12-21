# Uncann.ly

Get the most phonetically probable yet missing words of the English language.

Visit [http://uncannly.cfapps.io](http://uncannly.cfapps.io) for a demonstration.

Basically, two modes to find these words are presented.

In `random` mode, we generate words from scratch each time using a Markov chain of phonemes.

In `top` mode, the very most likely words possible to be generated by this same chain, pre-generated, are drawn from.

## Options

* **pool**

How many words to gather by the chosen mode. Default: 45.

* **selection**

When enabled, use the other mode to select within the pool.
When enabled, no value is provided, use the other mode, but select all (read: in `top` mode, scramble and introduce repeats; in `random` mode, sort). 

In top mode, you can add a selection value smaller or equal to the pool to lock down how many of them are returned, then increase the pool to increase the proportion of less probable words within that selection count. 

In random mode, take the same action to increase the proportion of *more* probable words within that selection count, by generating more and more random words that might be more probable than ones you'd already generated.

Default: disabled.

* **scoring method**

The method used to score words by, and filter out the lower scoring ones. Four methods exist in a 2×2 matrix relationship:

| operation \ value | total							 | average					 |
| ----------------- | ------------------ | ----------------- |
| multiplication		| `integral-product` | `mean-geometric`	 |
| addition					| `integral-sum`		 | `mean-arithmetic` |

1) `integral-product`: the probability from each phoneme to the next is continuously multiplied.
2) `integral-sum`: the probability from each phoneme to the next is continuously added (except that it's actually 1 minus each probability which gets summed, and then the reciprocal of that number so that we can sort the same direction as the other three methods). 
3) `mean-geometric`: like the integral product except that the nth root of the result is taken, where n is the number of phonemes up to that point.
4) `mean-arithmetic`: just the average of all probabilies thus far.

The "total" methods give a measure of "out of all the possible words, what is the actual chance of this word". Since the probability of a given next phoneme is never greater than 1, adding a new phoneme can only decrease the score. Therefore totalling methods are biased toward shorter words. 

The "average" methods do allow for new phonemes to actually increase the score of a word. For example, the word "jyɑtɚdʌnd" gets off to a really rough start, but the rest of the word consists of very common phoneme transitions. Average methods allow for weirder phoneme transitions to occur up front without nixing the pathway to generating words, and allow for longer words.

Scoring is required when filtering (one must filter by something). Filtering is optional for the `random` mode, but it is required for this most probable `top` mode, because the possibility space is too large to traverse without some filter. Therefore, scoring is required for `top` mode. 

The default scoring method is `integral-product`.

* **score threshold**

When specified, will not return words with scores (according to the current scoring method) lower than this threshold.

If you pass a value, it will be taken as the number of words to include in the pool. 

The value may be lower than the return count. You will just get more repeats than you might normally.

Words are currently limited to 20 letters regardless of any options.

* **unweighted**

Do not weight probabilities by frequency of words in the corpus.

* **unstressed**

Ignore stress levels of vowels.

* **exclude real**

Do not include words probable by pronunciation that do exist.

## Endpoint versions:

### /random

Query params:
* `unweighted`
* `exclude-real`
??????????????????????where did the rest of these all go????????????

e.g.

```
https://uncannly.cfapps.io/random?unweighted&exclude-real
"fɑɪtrɛθrikɑtɪvʌltʌn"
```

```
https://uncannly.cfapps.io/random
"pɑtɛndemɛðɛθ"
```

### /top

Query params:
* `pool`
* `selection`
* `scoring-method`
* `score-by-integral-product`
* `score-by-integral-sum`
* `score-by-mean-geometric`
* `score-by-mean-arithmetic`
* `score-threshold`
* `unweighted`
* `unstressed`
* `exclude-real`

e.g.

```
https://uncannly.cfapps.io/top?pool=500&selection=3&scoring-method=mean-arithmetic&score-threshold=0.2&unweighted&unstressed&exclude-real
["s", "kʌntʌn", "kʌliʌn"]
```

```
https://uncannly.cfapps.io/top
["wɑz (WAAS)", "wɚ (WE'RE(2))", "ɪŋ (ING)", "wɑr", "ɪz (IS)", ...] ????????????work stress into this
```

## Terminal script versions:

### bin/random

Arguments:
* `-u`, `--unweighted`
* `-x`, `--exclude-real`
????????????????????????????????where did everybody go??????????? and get stress right when you realize the bottom

e.g.

```
$ python bin/random.py -u -x
Y UW Z IH T AH Z
```

```
$ python bin/random.py
G EH R (GAIR)
```

### bin/words

Arguments:
* `-p`, `--pool`
* `-s`, `--selection`
* `-r`, `--scoring-method`
* `-m`, `--score-by-integral-product`
* `-a`, `--score-by-integral-sum`
* `-g`, `--score-by-mean-geometric`
* `-v`, `--score-by-mean-arithmetic`
* `-t`, `--score-threshold`
* `-u`, `--unweighted`
* `-i`, `--unstressed`
* `-x`, `--exclude-real`

e.g.

```
$ python bin/top.py -c 3 -r 500 -a -t 2.0 -u -i -x
K AH L IY AH N
K AH N T AH N
S
```

```
$ python bin/top.py
W AA1 Z (WAAS)
W ER1 (WE'RE(2))
IH1 NG (ING)
W AA1 R
IH1 Z (IS)
...
```