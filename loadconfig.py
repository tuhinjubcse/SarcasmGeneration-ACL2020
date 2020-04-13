import yaml

path = './comet-commonsense/config/config.yaml'

def loadConfigForROV():
	with open(path) as f:
		docs = yaml.load_all(f, Loader=yaml.FullLoader)
		for doc in docs:
			for k, v in doc.items():
				if k=="exception_vadarneg_words":
					exception_vadarneg_words=v
				elif k=="missing_vadarneg_words":
					missing_vadarneg_words=v
	return exception_vadarneg_words,missing_vadarneg_words

def loadConfigForRank():
	with open(path) as f:
		docs = yaml.load_all(f, Loader=yaml.FullLoader)
		for doc in docs:
			for k, v in doc.items():
				if k=="swap":
					swap_words=v
	return swap_words

def loadConfigForSentences():
	with open(path) as f:
		docs = yaml.load_all(f, Loader=yaml.FullLoader)
		for doc in docs:
			for k, v in doc.items():
				if k=="nonoverlap":
					nonoverlap_words=v
	return nonoverlap_words




def loadConfigForRetrieval():
	with open(path) as f:
		docs = yaml.load_all(f, Loader=yaml.FullLoader)
		for doc in docs:
			for k, v in doc.items():
				if k=="stop_words":
					stop_words = v[0].split(',')
				if k=="missing":
					missing = v
				if k=="quantifier":
					quantifier = v
				if k=="replacement":
					replacements = v
				if k=="start":
					start = v
				if k=="wrongNE":
					wrongNE = v

	return stop_words,missing,quantifier,replacements,start,wrongNE


def loadConfig(step):
	if step == 'ROV':
		return loadConfigForROV()
	elif step == 'Retrieve':
		return loadConfigForRetrieval()
	elif step == 'Sentences':
		return loadConfigForSentences()
	else:
		return loadConfigForRank()