from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from loadconfig import loadConfig
import sys
import os


def getWordNetAntonyms():
	m= {}
	for line in open('./data/antonyms.txt'):
		m[line.strip().split()[0]]= line.strip().split()[1]
	return m


def findIfnegationPresent(utterance):
	words = utterance.split()
	for w in words:
		if w=='not' or w=='never' or  w=='Not' or w=='Never':
			return w,True
	return '',False

def findIfendingwithnt(utterance):

	d = {"didn't": "did","don't": "do","doesn't":"does","can't": "can",
	"cannot":"can","wouldn't":"would","shouldn't":"should"}
	words = utterance.split()
	for w in words:
		if w in d:
			return w,d[w],True
		if w.lower() in d:
			return w,d[w.lower()].capitalize(),True
	return '','',False


def getAntonym(word):
	antonyms = getWordNetAntonyms()
	if word.lower() not in antonyms:
		synonymsset = []
		antonymsset = []
		for syn in wn.synsets(word.lower()):
			for l in syn.lemmas():
				synonymsset.append(l.name())
				if l.antonyms():
					antonymsset.append(l.antonyms()[0].name())
		if len(antonymsset)==0:
			for w in synonymsset:
				if w in antonyms:
					return antonyms[w.lower()]
			return "not "+word
		else:
			return antonymsset[0]
	else:
		return antonyms[word.lower()]


def ifTwoNegation(utterance):
	exception_vadarneg_words, missing_vadarneg_words= loadConfig('ROV')
	utterance = utterance.replace(',','')
	sid = SentimentIntensityAnalyzer()
	arr = []
	sent = word_tokenize(utterance)
	for i in range(len(sent)):
		w = sent[i]
		if w == 'no':
			continue
		ss = sid.polarity_scores(w)
		if (ss['neg']==1.0 or w in missing_vadarneg_words) and (w not in exception_vadarneg_words):
			arr.append((w,i,abs(ss['compound'])))
	if len(arr)==2:
		if abs(arr[0][1]-arr[1][1])==2:
			return [arr[0][0],arr[1][0]],True
		else:
			return [arr[1][0]],True
	else:
		return [],False


def isThereOnlyOneNegation(utterance):
	exception_vadarneg_words, missing_vadarneg_words= loadConfig('ROV')
	sid = SentimentIntensityAnalyzer()
	count = 0
	word = ''
	arr = []
	for w in word_tokenize(utterance):
		if w=='no':
			continue
		ss = sid.polarity_scores(w)
		if ss['neg']==1.0 and w not in exception_vadarneg_words:
			count = count+1
			if count<=1:
				word = w
			arr.append(word)
		elif w in missing_vadarneg_words and count==0:
			count = count+1
			if count<=1:
				word = w
	if count==1:
		return word,True
	return 'cant_change',False



#TODO In future work used improved negation
#Current style/sentiment transfer techniques are still at low accuracy
def reverse_valence(utterance):
	#directly handle these without going for complicated logic
	utterance = utterance.lower()
	utterance = utterance.replace(' i ',' I ')
	if 'should be' in utterance or 'would be' in utterance:
		return utterance.replace(' be ',' not be ').capitalize()
	if ' need to ' in utterance:
		return utterance.replace(' need to ',' need not ').capitalize()
	if 'hate' in utterance:
		return utterance.replace('hate','love').capitalize()
	if 'least' in utterance:
		return utterance.replace('least','most').capitalize()
	if utterance.endswith('lies.'):
		return utterance.replace('lies','truth').capitalize()

	utterance = utterance.replace(" don't "," do not ")

	#check if negation present , in terms of single or double words or not/n't words
	word,verdict = findIfnegationPresent(utterance)
	negword,replneg,verdict1 = findIfendingwithnt(utterance)
	words,verdict3 = ifTwoNegation(utterance)
	negative, verdict2 = isThereOnlyOneNegation(utterance)

	#handle case by case , give priority to remove not first
	# print("here1",utterance)
	if verdict == True:
		return utterance.replace(word+' ','')
	elif verdict1==True and verdict2==False:
		return utterance.replace(negword,replneg)
	elif verdict3==True:
		for w in words:
			if getAntonym(w).startswith('not'):
				continue
			utterance = utterance.replace(w,getAntonym(w))
		return utterance
	else:
		prev_utterance = utterance
		utterance = utterance.replace(negative,getAntonym(negative))
		#incase algorithm could not handle still try to negate
		#cases replace present tense verbs by appending a don't
		#cases replace unique words prefixing with un 
		if utterance == prev_utterance:
			text = word_tokenize(utterance)
			pos_text = pos_tag(text)
			for a,b in pos_text:
				if b == 'VBP':
					utterance = utterance.replace(a,"don't "+a)
					break
				if a.startswith('un'):
					utterance = utterance.replace(a,a[2:])
					break
		utterance = utterance.split()
		for i in range(len(utterance)):
			if utterance[i] == 'an' and utterance[i+1][0] not in ['a','e','i','o','u']:
				utterance[i] = 'a'
		utterance = ' '.join(utterance)
		return utterance.capitalize()

#print(reverse_valence(sys.argv[1]))
