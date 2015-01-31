# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 14:41:56 2015

@author: tania
"""

import random;
from math import *;

pos_words=[];
neg_words=[];
word_freq={};
sentences=[];
frequencies=[];

def is_vowel(ch):
     return ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u';
    
#counts total number of positive or negative words
def count_match(sentence,list_words):
   total=0;
   for w in list_wors:
        total+=sentence.count(w);
        
    return toatal;
    
def sentence_features(sentence):
    sent_freq=[count_match(sentence,pos_words),count_match(sentence,neg_words))];
    return sent_freq;  

#


def test_naive_Bayes(N,K,R):
    accuracy=0.0
    if N>0 and K>0 and R>0:
        labeled_names = ([(name[0],count_match(sentence,pos_words),count_match(sentence,pos_words) ) for name in names.words('data.txt')] ;
        random.seed(R);
        random.shuffle(labeled_names);
        featuresets = [(gender_features_new(n), gender) for (n,gender) in labeled_names];
        train_set = featuresets[:N]
        test_set = featuresets[N:];
        classifier = nltk.NaiveBayesClassifier.train(train_set);
        accuracy=nltk.classify.accuracy(classifier, test_set)*100;
        classifier.show_most_informative_features(K);
    else:
        print('ERROR IN K,R,N')
    return accuracy;
    
