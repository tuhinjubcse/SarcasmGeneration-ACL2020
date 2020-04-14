import requests, json
import nltk
import inflect


def correct_grammar(utterance1,utterance2,sex):
	utter = utterance1
	utterance1 = utterance1.split()
	utterance2 = utterance2.split()
	if sex=='':
		potential_name = utterance1[0]
		sex = getGenders(potential_name)[0][0]
	
	tags = nltk.pos_tag(utterance2)
	if tags[0][1]=='NNP':
		x = getGenders(utterance2[0])[0][0]
		if x=='male':
			utterance2[0]='he'
		elif x=='female':
			utterance2[0]='she'

	if utterance1[0].lower() in ['i','my']:
		if utterance2[0].lower() in ['his','her']:
			utterance2[0]='My'
		if utterance2[0].lower() in ['he','she'] and utterance2[1] in ['is','was']:
			utterance2[0]='I'
			utterance2[1] = 'am'
		if utterance2[0].lower() in ['he','she'] and utterance2[1] not in ['makes','stands']:
			utterance2[0]='I'
		for i in range(1,len(utterance2)):
			if utterance2[i] in ['his','her'] and utterance2[i-1]=='for':
				utterance2[i]='my'

	elif sex == 'male' and utterance2[0].lower() in ['her','my']:
		utterance2[0]='his'
	elif sex == 'male' and utterance2[0].lower()=='i' and utterance2[1].lower()=='am':
		utterance2[0]='he'
		utterance2[1]='is'
	elif sex == 'male' and utterance2[0].lower()in ['she','i']:
		utterance2[0]='he'
	elif sex == 'female' and utterance2[0].lower() in ['his','my','him']:
		utterance2[0]='her'
	elif sex == 'female' and utterance2[0].lower()=='i' and utterance2[1].lower()=='am':
		utterance2[0]='she'
		utterance2[1]='is'
	elif sex == 'female' and utterance2[0].lower() in ['he','i']:
		utterance2[0]='she'
	else:
		flag = False
		if utterance1[0].lower() not in ['his','her']:
			if utterance2[0].lower() in ['his','her']:
				utterance2[0]='My'
		if utterance1[0].lower() not in ['he','she'] and (sex!='female'):
			if utterance2[0].lower() in ['he','she'] and utterance2[1] in ['is','was']:
				utterance2[0]='I'
				utterance2[1] = 'am'
			if utterance2[0].lower() in ['he','she']:
				if utterance2[0].lower()=='he' and utterance2[1].lower()=='has':
					utterance2[0] = 'I'
					utterance2[1] = 'have'
				else:
					if utterance2[0].lower() in ['he','she']:
						for k in range(1,len(utterance2)):
							if utterance2[k]=='his' and utterance2[k-1][0]!='a':
								utterance2[k]='my'
							if utterance2[k]=='her':
								utterance2[k]='my'
					utterance2.pop(0)
					flag = True

			for i in range(1,len(utterance2)):
				if utterance2[i] in ['his','her'] and utterance2[i+1]=='to' and flag==False:
					utterance2[i]='my'
				elif utterance2[i] in ['his','her'] and utterance2[i+1]=='to':
					utterance2[i]='me'
	
	if utterance2[0]=='I':
		for i in range(1,len(utterance2)):
			if utterance2[i]=='your':
				utterance2[i]='my'

	c = 0
	for i in range(0,len(utterance2)):
		if utterance2[i] in ['his','her']:
			c = c+1

	if c==2:
		for i in range(0,len(utterance2)):
			if c==2 and utterance2[i] in ['his','her']:
				utterance2[i]='me'
				c = c-1
			if c==1 and utterance2[i] in ['his','her']:
				if utterance2[0]=='I':
					utterance2[i]='myself'
				else:
					utterance2[i]='my'
				c = c-1

	utterance2 =  ' '.join(utterance2).capitalize()
	if 'I am ' in utterance2 and ' his ' in utterance2:
		utterance2 = utterance2.replace(' his ', ' my ')
	if 'I am ' in utterance2 and ' her ' in utterance2:
		utterance2 = utterance2.replace(' her ', ' my ')
	if 'I ' in utterance2 and ' his ' in utterance2:
		utterance2 = utterance2.replace(' his ', ' my ')
	if 'I ' in utterance2 and ' her ' in utterance2:
		utterance2 = utterance2.replace(' her ', ' my ')
	if 'I ' in utterance2 and ' he ' in utterance2:
		utterance2 = utterance2.replace(' he ', ' I ')
	if 'I ' in utterance2 and ' she ' in utterance2:
		utterance2 = utterance2.replace(' she ', ' I ')



	if utterance1[0] not in ['I','My','i','my']:
		utterance2= utterance2.replace('You are ','I am ')
		utterance2= utterance2.replace('you are ','I am ')
		utterance2= utterance2.replace('made you ','made me')
		utterance2= utterance2.replace('gave you ','gave me')
		utterance2= utterance2.replace('told you ','told me')
		utterance2= utterance2.replace('You ','I ')
		if 'been' not in utterance2:
			utterance2= utterance2.replace(' you ',' I ')
		utterance2= utterance2.replace('we should','I will')
		utterance2= utterance2.replace('Their ','My ')
		utterance2= utterance2.replace('I is','I am')
		utterance2= utterance2.replace(' is he ',' am I ')

	if ' i ' in utter.lower() and ' him was ' in utterance2 or ' her was ' in utterance2:
		utterance2 = utterance2.replace(' him was ',' you is ')
		utterance2 = utterance2.replace(' her was ',' you is ')

	utterance2 = utterance2.replace(' i ',' I ')
	return utterance2,sex




def getGenders(names):
	url = ""
	cnt = 0
	if not isinstance(names,list):
		names = [names,]
	
	for name in names:
		if url == "":
			url = "name[0]=" + name
		else:
			cnt += 1
			url = url + "&name[" + str(cnt) + "]=" + name
		

	req = requests.get("https://api.genderize.io?" + url)
	results = json.loads(req.text)
	
	retrn = []
	for result in results:
		if result["gender"] is not None and result["probability"]>0.9 and (names[0] not in ["haven't","we've","Haven't","waven't","Drinking","Can","Sunday"]):
			retrn.append((result["gender"], result["probability"], result["count"]))
		else:
			if names[0] in ['Mom','mom']:
				return [(('female',1.0,100))]
			else:
				retrn.append((u'None',u'0.0',0.0))
	return retrn

