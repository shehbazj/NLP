# input : 3 files 
# 1. Grammar
# 2. Lexicon
# 3. sentence
# from 1 and 2, create a chart parser
# from 3, take one input sentence at a time, and check if NLTK parsing happens or not
#

import nltk
import sys

with open('Grammar', 'r') as myfile:
    grammar=myfile.read()#.replace('\n', '')

with open('Lexicon', 'r') as myfile:
    lexicon=myfile.read()#.replace('\n', '')


data = grammar + lexicon
data = data[:-1]

#print (data)

grammar = nltk.grammar.CFG.fromstring(data)

sentences = tuple(open('Positives','r'))
#sentences = tuple(open('Negatives','r'))

for raw_sentence in sentences:
    sentence = nltk.tokenize.word_tokenize(raw_sentence)
    print ( raw_sentence[:-1] )
   # parser = nltk.parse.BottomUpChartParser(grammar, trace=True )
    parser = nltk.parse.BottomUpChartParser(grammar )
    if not parser.parse_all(sentence):
        print ( "No parses" )
    for t in parser.parse_all(sentence):
        print(t)
