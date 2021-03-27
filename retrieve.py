import nltk
import yaml
import string
import json
from loadconfig import loadConfig
import os
import sys
import ast
from urllib.parse import quote
nltk.download('maxent_ne_chunker')
nltk.download('words')

sys.path.append(os.getcwd()+'/comet-commonsense')
m = {}
words = []

from pattern.en import conjugate, lemma, lexeme, PRESENT, PAST, SG,PARTICIPLE


def choppunc(stri):
	if stri.endswith('.') or stri.endswith('?') or stri.endswith('!'):
		return stri[:-1]
	else:
		return stri


def preprocess(utterance):

	stop_words, missing, quantifier, replacements, start, wrongNE = loadConfig(
	    'Retrieve')
	sent = choppunc(utterance)
	b = sent.split()
	b[0] = b[0].lower().capitalize()
	c = nltk.pos_tag(b)
	d = nltk.ne_chunk(c, binary=True)
	m = {}
	for val in d:
		if str(type(val)) == "<class 'nltk.tree.Tree'>":
			for v in val:
				m[v[0]] = val.label()
		else:
			m[val[0]] = "NNE"
	for u, v in c:
		if (v == 'NNP' and m[u] == 'NE' and u not in wrongNE) or (v == 'CD' and u not in quantifier) or u == ',' or u == 'U.S':
			stop_words.append(u.lower())

	x = sent.lower().split()

	elem = []
	for i in range(len(x)):
		w = x[i]
		if (w not in stop_words):
			elem.append(w)

	if len(elem) >= 5 and missing[0] in elem:
		elem = ' '.join(elem).replace(' .', '.')
		elem = elem.replace(' '+missing[0], '')
	else:
		elem = ' '.join(elem).replace(' .', '.')


	for v in start:
		if elem.startswith(v):
			elem = elem.replace(v+' ', '')

	for v in replacements:
		rep = v.split(',')
		if rep[0] in elem:
			elem = elem.replace(rep[0], rep[1])

	return elem


def getCommonSense(utterance):
	os.system('python comet-commonsense/scripts/generate/generate_conceptnet_arbitrary.py --model_file comet-commonsense/pretrained_models/conceptnet_pretrained_model.pickle --input "'+utterance+'" --output_file output.json --device 0 --sampling_algorithm beam-5')
	output = json.load(open('output.json', "r"))
	return output[0]['Causes']['beams']


def retrieveCommonSense(utterance):
	modified_utterance = preprocess(utterance)
	return getCommonSense(modified_utterance)



print(retrieveCommonSense(sys.argv[1]))




