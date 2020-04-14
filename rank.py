import torch
import numpy
from sentence_retriever import getSentences
from grammar import correct_grammar
from loadconfig import loadConfig
import random
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"



correct_phrase = loadConfig('Rank')


def getRoberta():
	roberta = torch.hub.load('pytorch/fairseq', 'roberta.large.mnli')
	roberta.cuda()
	roberta.eval()
	return roberta

def getContradictionScores(roberta,sentences,rov):
	scores = []
	gender = ''
	for sent in sentences:
		sent,gender = correct_grammar(rov,sent,gender)
		tokens = roberta.encode(rov, sent)
		value = roberta.predict('mnli', tokens).cpu().detach().numpy()
		value = round(value[0].tolist()[0],3)
		scores.append((value,sent.capitalize()))

	return scores


def rank_sentences_based_on_contradiction(roberta,sentences,rov):
	scores = getContradictionScores(roberta,sentences,rov)
	scores.sort(key = lambda x: (x[0],-len(x[1].split())),reverse=True)
	return scores[0]

def getSentenceforNSI(sentences,rov,commonsense,extra=''):
	sentences = getSentences(commonsense,'',False)
	return random.choice(sentences)


def rankContext(roberta,rov,commonsense,extra=''):
	sentences = getSentences(commonsense,rov)
	if extra!='':
		for i in range(len(sentences)):
			if commonsense in correct_phrase:
				replacement = commonsense+' '+extra
			else:
				replacement = extra+' '+commonsense
			if replacement not in sentences[i]:
				sentences[i] = sentences[i].lower().replace(commonsense,replacement).capitalize()
	mostcontradictory = rank_sentences_based_on_contradiction(roberta,sentences,rov)
	x = mostcontradictory[1].capitalize()
	x = x.replace(' i ',' I ')
	return x







	
