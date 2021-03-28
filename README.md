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

> Copyright (c) 2021 Ron Urbach
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
