# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import nltk
from nltk import book
from nltk.tag import StanfordPOSTagger
import pandas
import winsound
import unicodedata
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

jar = 'stanford-postagger-full-2018-02-27/stanford-postagger-3.9.1.jar'
model = 'stanford-postagger-full-2018-02-27/models/french.tagger'
stopWords = set(nltk.corpus.stopwords.words('french'))|set(nltk.corpus.stopwords.words('english'))
findephrase = ['.','[',']','?','!','...','."','".','.".','\n','','?"','!"','!--']
findeprop = [',','(',')','"',';'," '","' ",',"',':',',--','--"']
findemot = ['\n',' ']
FailWords = ['mr','mme','chapter','mrs','les']
toreplace = ['Ã ','Ã¢','Ã©','Ã¨','Ãª','Ã«','Ã®','Ã¯','Ã´','Ã¶','Ã¹','Ã»','Ã¼','Ã§','Â°','â€™','Ã']
replacement = ['à','â','é','è','ê','ë','î','ï','ô','ö','ù','û','ü','ç','°',"'",'à']
seed = 7
validation_size = 0.2
bgm = nltk.collocations.BigramAssocMeasures()

def defparameter(words):
    store = ((words)//800)
    if store <25:
        return 25
    elif store > 300:
        return 300
    else :
        return store

def motsfrequents(text,n):
    fdist = nltk.FreqDist(text)
    store = fdist.most_common(n)
    return [w[0] for w in store]

def motspertinents(text,n):
    store = motsfrequents(text,n)
    potents = [text[i] for i in range(1,len(text)) if not text[i].islower() and
               not text[i-1] in findephrase and text[i].isalpha() and 
               len(text[i])>2 and text[i].lower() not in stopWords]
    return [w for w in store if w in potents]
    
def placeDansLaPhrase(text,i):
    j = i
    while j>0:
        if text[j] in findephrase:
            return i-j
        j -= 1
    return -100000

def placeDansLaProp(text,i):
    j = i
    while j>=0:
        if text[j] in findephrase + findeprop:
            return i-j
        j -= 1
    return -100000

def createY(text,actors):
    Y = []
    for i in range(len(text)//2):
        if text[i] in actors:
            Y += [1]
        else:
            Y += [0]
    return Y

def isin(mot,liste):
    if mot in liste:
        return 10
    return -10

def createX(text):
    X = []
    motsfreq = motsfrequents(text,30)
    motspert = motspertinents(text,50)
    for i in range(len(text)//2):
        mot = text[i]
        X += [[len(mot),i,text.index(mot),placeDansLaPhrase(text,i),placeDansLaProp(text,i),isin(mot,motsfreq),isin(mot,motspert)]]
    return X

def createtestX(text):
    X = []
    motsfreq = motsfrequents(text,30)
    motspert = motspertinents(text,50)
    for i in range(len(text)//2,len(text)):
        mot = text[i]
        X += [[len(mot),i,text.index(mot),placeDansLaPhrase(text,i),placeDansLaProp(text,i),isin(mot,motsfreq),isin(mot,motspert)]]
    return X

def actors(text,parameter=0):
    words = len(text)
    if parameter == 0:
        parameter = defparameter(words)
    #if isenglish(text):
    #    tags = nltk.pos_tag(text)
    #else:#on suppose alors que le texte est en français
    #    pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
    #    tags = pos_tagger.tag(text)
    finder = nltk.collocations.BigramCollocationFinder.from_words(text)
    scored = finder.score_ngrams(bgm.likelihood_ratio)
    freq = motsfrequents(text,parameter)
    init = [freq[i] for i in range(len(freq)) if freq[i] not in findephrase+findeprop+findemot]
    debut = motspertinents(text,parameter)
    inter = []
    for i in range(len(debut)):
        mot = debut[i].lower()
        if (not mot in stopWords) and (not mot in FailWords):
            inter += [mot]
    final = []
    notin = []
    score = 100
    k = 0
    while score >= 100:
        for i in range(len(init)):
            for j in range(len(inter)):
                if (init[i].lower() == scored[k][0][0].lower()) and (inter[j] == scored[k][0][1].lower()):
                    final += [init[i]+" "+inter[j]]
                    notin += [j]
        for i in range(len(inter)):
            for j in range(len(init)):
                if (inter[i] == scored[k][0][0].lower()) and (init[j].lower() == scored[k][0][1].lower()):
                    final += [inter[i]+" "+init[j]]
                    notin += [i]
        score = scored[k][1]
        k+=1
    for i in range(len(inter)):
        if i not in notin:
            final += [inter[i]]
    final = reduce(final)
    #frequency = 500
    #duration = 500 
    #winsound.Beep(frequency, duration)
    return regroup(final)

def reduce(liste):
    liste += ['/n']#random mot dont on sait qu'il ne se trouve pas dans liste
    newliste = []
    for i in range(len(liste)-1):
        isalone = True
        for j in range(i+1,len(liste)):
            if liste[i].lower() == liste[j].lower():
                isalone = False
        if isalone:
            newliste += [liste[i]]
    return newliste

def regroup(liste):
    liste += ['/n']#random mot dont on sait qu'il ne se trouve pas dans liste
    for i in range(len(liste)-1):
        for j in range(i+1,len(liste)):
            if ' ' in liste[i] and ' ' in liste[j]:
                num1 = liste[i].split(' ')
                num2 = liste[j].split(' ')
                if num1[0].lower() == num2[-1].lower():
                    num2.pop()
                    liste.pop(j)
                    liste.pop(i)
                    liste.pop()
                    toappend = ''
                    for i in range(len(num2)):
                        toappend+=num2[i]+' '
                    for j in range(len(num1)):
                        toappend+=num1[j]
                        if j != len(num1)-1:
                            toappend += ' '
                    liste += [toappend]
                    return regroup(liste)
                if num2[0].lower() == num1[-1].lower():
                    num1.pop()
                    liste.pop(j)
                    liste.pop(i)
                    liste.pop()
                    toappend = ''
                    for i in range(len(num1)):
                        toappend+=num1[i]+' '
                    for j in range(len(num2)):
                        toappend+=num2[j]
                        if j != len(num2)-1:
                            toappend += ' '
                    liste += [toappend]
                    return regroup(liste)
    liste.pop()
    return liste

def cleaning(word):
    for i in range(len(toreplace)):
        word = word.replace(toreplace[i],replacement[i])
    return word
    
def txtToUsableText(file):
    file = open(file)
    reading = file.read()
    text = nltk.word_tokenize(reading)
    words = [cleaning(text[i]) for i in range(len(text))]
    return words

def isenglish(text):#text sous forme de liste de str
    wcount = 0
    lcount = 0
    for word in text:
        for letter in word:
            if letter == 'w':
                wcount +=1
            lcount +=1
    taux = wcount/lcount
    if taux>0.012:
        return True
    else:
        return False
    
        
        

#X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(createX(book.text2), createY(book.text2,actors2), test_size=validation_size, random_state=seed)
#DTC = DecisionTreeClassifier()
#DTC.fit(X_train, Y_train)
#predictions = DTC.predict(X_validation)
#print(accuracy_score(Y_validation, predictions))
#print(confusion_matrix(Y_validation, predictions))