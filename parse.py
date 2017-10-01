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

print (data)

#data2 = """
#S -> NP VP
#PP -> P NP
#NP -> DET N | N | NP PP
#VP -> V NP | VP PP
#DET -> 'the'
#N -> 'Nadia' | 'man' | 'eggplant'
#V -> 'rewarded'
#P -> 'with'
#"""

grammar = nltk.grammar.CFG.fromstring(data)

with open('Sentences', 'r') as myfile:
    sentences = tuple(open('Sentences','r'))

for raw_sentence in sentences:
#    print ( raw_sentence )
    #raw_sentence = "Nadia rewarded the man with the eggplant"
    #raw_sentence1 = "Nadia rewarded the man with the eggplant"
    #raw_sentence = raw_sentence[:-1]
    #print ( raw_sentence [:-1])
#    sentence = nltk.tokenize.word_tokenize(raw_sentence[:-1])
    sentence = nltk.tokenize.word_tokenize(raw_sentence)
    print ( raw_sentence[:-1] )
    parser = nltk.parse.BottomUpChartParser(grammar)
    for t in parser.parse_all(sentence):
        print(t)
