import nltk;
import random;
from math import *;
import csv;
#import numpy as np
csv.field_size_limit(2147483647)#increase python fild size


# label position=1 , sentence position=11
#read  train data file and store tuple(label,sentence) into a list

def read_csv(filename):
    raw_data = csv.reader(open(filename, newline=''), delimiter='"', quotechar='|')
    tuple_list=[];
    for row in raw_data:
        tuple_list.append((row[1],row[11]));
    return tuple_list

#list of tuples(label,sentence)
labeled_sentences=read_csv('training.1600000.processed.noemoticon.csv');#list of tuples(label,sentence)

#read txt file
def read_txt(filename):
    positive=open(filename,'r'); 
    lines=positive.readlines();
    words=[line[:-1] for line in lines]
    return words;

pos_words= read_txt('positive.txt')   
neg_words=read_txt('negative.txt')  
       
#counts total number of positive or negative words
def count_match(sentence,list_words):
   total=0;
   for w in list_words:
        total+=sentence.count(w);
   return total;

def find_new_words(labeled_sentences):
    #default dictionary for all found words
    poswordcounts = defaultdict(int)
    negwordcounts = defaultdict(int)
    for labeled_sentence in labeled_sentences:
        if labeled_sentence[0] == 4:
            for w in labeled_sentence:
                poswordcounts += 1
        elif labeled_sentence == 0:
            for w in labeled_sentence:
                negwordcounts+=1
    for w in poswordcounts:
        if (poswordcounts[w] - negwordcounts[w]) > 0:
            pos_words.append(w)
        elif (poswordcounts[w] - negwordcounts[w]) < 0:
            neg_words.append(w)
            

'''def sentence_features(sentence):
    sent_freq=[count_match(sentence,pos_words),count_match(sentence,neg_words))];
    return sent_freq; ''' 

def test_naive_Bayes(N,K,R):
    accuracy=0.0
    if N>0 and K>0 and R>0:
        random.seed(R);
        random.shuffle(labeled_sentences);
        featuresets =[(l,count_match(sent,pos_words),count_match(sent,pos_words)) for (l,sent) in labeled_sentences] ;
       # featuresets = [(gender_features_new(n), gender) for (n,gender) in labeled_names];
        train_set = featuresets[:N]
        test_set = featuresets[N:];
        classifier = nltk.NaiveBayesClassifier.train(train_set);
        accuracy=nltk.classify.accuracy(classifier, test_set)*100;
        classifier.show_most_informative_features(K);
    else:
        print('ERROR IN K,R,N')
    return accuracy;
    
#print(test_naive_Bayes(600000,10,30))
