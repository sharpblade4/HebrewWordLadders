# Hebrew Word Ladders
### Description
A computed solver for the hebrew version of a word-ladders game
 (also known as [doublets](https://en.wikipedia.org/wiki/Word_ladder)) which was invented by Lewis Carroll,
 where given a word and a destination word one needs to find a chain of
 legal words with [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) 1 between each.

### About
This was used as a part of an activity for "passover seder". See attached slides under "res".

### Usage
#### One time setup
Assuming you have python3 installed on your machine.
```
git clone https://github.com/sharpblade4/HebrewWordLadders.git  &&\
cd HebrewWordLadders  &&\
python -m pip install -r requirements.txt
```
#### Run
`./src/main.py עבדות חירות`

### License
**MIT** : basically use as you please but give credit
(especially for the hebrew words see documentation for instructions).
