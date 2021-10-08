#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:12:55 2021

@author: kshama.singh
"""


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


paragraph = open("../Lemmatization/Lemmatization.txt", 'r').read()
#print(paragraph)

# Preparing the sentences
def processData_SentencesTokenize(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    return sentences


# Preparing the words
def processData_WordTokenize(paragraph):
    words = nltk.word_tokenize(paragraph)
    return words

# Preparing the dataset
def processData_dataset(sentences, words, lemmatize):
    for i in range(len(sentences)):
        word = nltk.word_tokenize(sentences[i])
        word = [lemmatize.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
        sentences[i] = ' '.join(words)
    return sentences

sentences = processData_SentencesTokenize(paragraph);

words = processData_WordTokenize(paragraph);

lemmatize = WordNetLemmatizer()

dataset = processData_dataset(sentences, words, lemmatize);

#print(dataset)