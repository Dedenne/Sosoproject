# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Tue Mar 20 10:06:02 2018)---
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
debugfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
import nltk
from nltk import book
text1.concordance("whale")
book.text1.concordance("whale")
book.text1.similar("I")
book.text1.similar("whale")
book.text1.similar("mast")
book.text1.similar("kill")
book.text1.concordance("kill")
book.text1.concordance("water")
book.text1.similar("water")
book.text1.common_contexts("water","land")
book.text1.common_contexts(["water","land"])
book.text1.dispersion_plot(["water","land","I","Moby","kill"])
book.text1.generate()
book.text1.generate("I")
fdist = FreqDist(book.text1)
fdist = nltk.FreqDist(book.text1)
fdist.most_common(20)
fdist.most_common(30)
fdist.most_common(40)
signi = [w[0] for w in fdist.most_common(100)] 
signi
signi = [w[0] for w in fdist.most_common(100) if len(w[0])>4]
signi
signi = [w[0] for w in fdist.most_common(50) if len(w[0])>2]
signi
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
signi = [w[0] for w in fdist.most_common(50) if len(w[0])>2 and not(w[0] in stopWords)]
signi
signi = [w[0] for w in fdist.most_common(100) if len(w[0])>2 and not(w[0] in stopWords)]
signi
len(nltk.set(book.text1))/len(book.text1)
len(set(book.text1))/len(book.text1)
len(book.text1)/len(set(book.text1))
len(book.text6)/len(set(book.text6))
len(book.text5)/len(set(book.text5))
len(book.text2)/len(set(book.text2))
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text[i].islower() and not book.text[i-1] in [".","?","!","..."]])
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."]])
Acteurs
Acteurs1
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."] and book.text1[i] in fdist.most_common(1000)])
fdist = FreqDist(book.text1)
fdist = nltk.FreqDist(book.text1)
fdist
mostcommon1 = fdist.mostcommon(1000)
mostcommon1 = fdist.most_common(1000)
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."] and book.text1[i] in mostcommon1])
Acteurs1
mostcommon1
mostcommon1 = [w[0] for w in mostcommon1]
mostcommon1
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."] and book.text1[i] in mostcommon1])
Acteurs1
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."] and book.text1[i] in mostcommon1] and book.text1[i].isalpha()])
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."] and book.text1[i] in mostcommon1 and book.text1[i].isalpha()])
Acteurs1
mostcommon1 = fdist.most_common(500)
mostcommon1 = [w[0] for w in mostcommon1]
Acteurs1 = set([book.text1[i] for i in range(1,len(book.text1)) if not book.text1[i].islower() and not book.text1[i-1] in [".","?","!","..."] and book.text1[i] in mostcommon1 and book.text1[i].isalpha()])
Acteurs1
Acteurs1 = motspertinents(book.text1,400)
import temp.py
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
Acteurs1 = motspertinents(book.text1,400)
Acteurs1
book.text1
book.text1[:100]
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
createX(['I','know','you','want','me',',','you','know','I','want','you'])
createX(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
X = createX(book.text1)
X[:10]
book.text1.index('whale')
['a'] +['b']
1 in [1]
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
testX = createtestX(book.text1)
predictions2 = DTC.predict(testX)
prediction[:15]
predictions2[:15]
predictions2[:100]
predictions2[100:200]
predictions2[200:300]
predictions2[200:1000]
predictions2.index(1)
predictions2.find(1)
import numpy as np
np.sum(predictions2)
runfile('C:/Users/rapha/Downloads/Solypse - CSVtoGraph.py', wdir='C:/Users/rapha/Downloads')
predictions2[3000:4000]
np.sum(predictions2[:len(predictions2//2)])
np.sum(predictions2[:len(predictions2//4)])
np.sum(predictions2[:len(predictions2//8)])
np.sum(predictions2[:len(predictions2//16)])
np.sum(predictions2[:len(predictions2//32)])
len(predictions2)
len(book.text1)
np.sum(predictions2[:len(predictions2)//2])
np.sum(predictions2[len(predictions2)//2:])
np.sum(predictions2[len(predictions2)//2:3*len(predictions2)//4])
np.sum(predictions2[3*len(predictions2)//4:])
np.sum(predictions2[7*len(predictions2)//8:])
np.sum(predictions2[15*len(predictions2)//16:])
predictions2 == 1
indexes = [i if predictions2[i] == 1]
indexes = [i if predictions2[i] == 1 for i in range(len(predictions2))]
indexes = [i for i in range(len(predictions2))if predictions2[i] == 1]
indexes
length = len(book.text1)
actorpot = [book.text1[length//2+indexes[i]] for i in range len(indexes)]
actorpot = [book.text1[length//2+indexes[i]] for i in range(len(indexes))]
actorpot
motspertinents(book.text2,30)
motspertinents(book.text2,100)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
testX = createtestX(book.text2)
predictions2 = DTC.predict(testX)
length = len(book.text2)
indexes = [i for i in range(len(predictions2))if predictions2[i] == 1]
actorpot = [book.text1[length//2+indexes[i]] for i in range(len(indexes))]
actorpot = [book.text2[length//2+indexes[i]] for i in range(len(indexes))]
actorpot
'Edward' in actorpot
stopwords()
stopwords(english)
stopwords(en)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
actors(book.text2)
actors(book.text3)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text3)
actors(book.text4)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
scored[1]
scored[(',','and')]
scored.(',','and')
(',','and') in scored
scored[',']
scored(',')

scored[1:3]
scored[1:3][1]
scored[0][1:3]
scored[0]
"'" in scored[0][0]
"'"+'s'
"'" in scored[0][0][0]
scored[0][0][0]
scored[0][1]
scored[100][1]
scored[100][0]
scored[0:100]
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
motspertinents(book.text1,300)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
actors(book.text2)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text2)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text2)
actors(book.text3)
actors(book.text4)
actors(book.text5)
actors(book.text6)
actors(book.text7)
actors(book.text8)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text8)
len(book.text8)
len(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text8)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text8)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text8)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text8)
actors(book.text2)
len(book.text2)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text2)
actors(book.text3)
len(book.text3)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text3)
actors(book.text4)
len(book.text4)
(145735-21000)//800
(260000 - 21000)//800
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text4)
actors(book.text5)
book.text5
book.text5[:1000]
actors(book.text6)
actors(book.text7)
book.text7[:100]
actors(book.text8)
book.text8[:100]
actors(book.text9)
book.text9[:100]
len(book.text9)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text9)
actors(book.text1)
actors(book.text2)
actors(book.text3)
GISHED = open('GISHED.txt')
GISHED.read()
GISHED = open('GISHED.txt')
GISHED.read()
GISHED.read(5)
GISHED.read()
GISHED = open('GISHED.txt')
GISHED.read()
GISHED = open('GISHED.txt')
GISHED.read(5)
GISHED.read(1)
GISHED.read(6)
GISHED.read(100)
'a' + 'b'
GISHED = open('GISHED.txt')
GISHED.read(1)
word = 'ab'
word += 'c'
word
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
s = 'Découvrez tous les logiciels à télécharger'
s
s1 = unicode(s,'utf-8')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
textBook = txtToUsableText('GISHED.txt')
motspertinents(textBook,100)
motspertinents(textBook,1000)
motspertinents(textBook,500)
motspertinents(textBook,300)
motspertinents(textBook,200)
len(textBook)
motspertinents(textBook,150)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
test = 'Ich bin ein Berliner'
test.replace('bin','durch')
replace
test
test.replace('strudel','ert')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
GISHED.open()
open('GISHED.txt')*
open('GISHED.txt')
test = open('GISHED.txt')
test.read(250)
test.read(1000)
test.read(100)
test = open('GISHED.txt')
test.read(1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
1 in [2]+[1]
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
actors(txtToUsableText('UnitedeRecherche.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
actors(txtToUsableText('UnitedeRecherche.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
actors(txtToUsableText('UnitedeRecherche.txt'))
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
import numpy as np
np.ppcm(365,1111)
pgcd(1,2)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(book.text1)
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
a = ['grenelle', 'directive', 'shf']
len(a)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('GISHED.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('ManyGraphs.txt'))
actors(txtToUsableText('BiographieEng.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('BiographieEng.txt'))
len(txtToUsableText('BiographieEng.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('BiographieEng.txt'))
actors(txtToUsableText('List.txt'))
read = txtToUsableText('List.txt')
file = open('List.txt')
file.encoding
file.encoding()
file = open('List.txt','r')
file.encoding()
file.encoding
file.decode('cp1252')
file
file2 = open("BiographieEng.txt")
file2
len(txtToUsableText('BiographieEng.txt'))
read = txtToUsableText('List.txt')
read = open('List.txt')
reading = read.read(1)
actors(txtToUsableText('List.txt'))
test = 'hydraulic Machinery'.split(' ')
test
test.pop()
testtest = 'hydraulic Machinery'.split(' ')
test = 'hydraulic Machinery'.split(' ')
test.pop(0)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
test[-1]
test+test
test = 'hydraulic Machinery'.split(' ')
test+test
str(test) +str(test)
test = 'lolilol  lol'
test.split(' ')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
test = 'lolilol lol '
test.split(' ')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('List.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('BiographieEng.txt'))
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors(txtToUsableText('BiographieEng.txt'))
import nltk
nltk.word_tokenize(open('Biographie.txt'))
nltk.word_tokenize(open('BiographieEng.txt'))
nltk.word_tokenize(txtToUsableText('BiographieEng.txt'))
testfile = open('UnitedeRecherche.txt')
testread = testfile.read()
nltk.word_tokenize(testread)
txtToUsableText('UnitedeRecherche')
txtToUsableText('UnitedeRecherche.txt')
test = txtToUsableText('UnitedeRecherche.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('UnitedeRecherche.txt')
test
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('UnitedeRecherche.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('UnitedeRecherche.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('UnitedeRecherche.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('UnitedeRecherche.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('UnitedeRecherche.txt')
test = txtToUsableText('BiographieEng.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('BiographieEng.txt')
test
test = txtToUsableText('BiographieEng.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
test = txtToUsableText('BiographieEng.txt')
test
test = txtToUsableText('BiographieEng.txt')
test = txtToUsableText('unitedeRecherche.txt')
test
test = 'Ã'
test.replace('Ã','à')
test = txtToUsableText('unitedeRecherche.txt')
nltk.pos_tag(test)
nltk.help.upenn_tagset()
test = txtToUsableText('BiographieEng.txt')
nltk.pos_tag(test)
text = ['lolilol','lol']
test = [word for word in text]
test
1/2
text =txtToUsableText('BiographieEng.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
isenglish(text)
text =txtToUsableText('ManyGraphs.txt')
isenglish(text)
text
text =txtToUsableText('UnitedeRecherche.txt')
isenglish(text)
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors('UnitedeRecherche.txt
actors('UnitedeRecherche.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors('UnitedeRecherche.txt')
actors('ManyGraphs.txt')
runfile('C:/Users/rapha/.spyder-py3/temp.py', wdir='C:/Users/rapha/.spyder-py3')
actors('ManyGraphs.txt')
actors('UnitedeRecherche.txt')