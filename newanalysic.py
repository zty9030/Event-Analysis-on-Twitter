import operator
import string
import pandas as pd
POSI = 'positive-words.txt'
NEGA = 'negative-words.txt'
def loadWords(path):
	print('loading words from file')
	infile = open(path,'r',0);
	wordlist = infile.read().split('\n')
	print ' ', len(wordlist),'words loaded.';
	return wordlist;

plist = loadWords(POSI)
pdic = dict(zip(plist,[0]*len(plist)))
nlist = loadWords(NEGA)
ndic = dict(zip(nlist,[0]*len(nlist)))
olist = plist+nlist
df = pd.read_csv('.txt')
dftext = df['Text']
print len(dftext),'tweets loaded'
psum = 0;
nsum = 0;
total = 0;
a=1
for line in dftext:
	print a
	line = line.lower();
	words = line.split();
	for i in olist:	
		if i in words:
			total +=1;
			break;
	for i in plist:
		if i in words:
			psum +=1;
			pdic[i]+=1
			break;
	for i in nlist:
		if i in words:
			nsum +=1;
			ndic[i]+=1
			break;
	a+=1
sorted_p = sorted(pdic.items(), key=operator.itemgetter(1))
sorted_n = sorted(ndic.items(), key=operator.itemgetter(1))
print 'total:', total; 
print 'p:',psum;
print sorted_p[-20:]
print 'n:',nsum;
print sorted_n[-20:]
