from reverse import reverse_valence
from retrieve import retrieveCommonSense
from rank import rankContext , getRoberta
import sys

roberta = getRoberta()

count = 0
f = open('FM-output.txt','a')
for a  in open('done.txt'):
	count = count+1
	if count<=140:
		continue
	utterance = a.strip() #sys.argv[1]
	rov = reverse_valence(utterance).capitalize()
	op = retrieveCommonSense(a[:-1])
	commonsense, extra = op[0], op[1]
	mostincongruent = rankContext(roberta,rov,commonsense,extra)
	sarcasm = rov + ' '+ mostincongruent
	f.write(sarcasm+'\n')
	print(sarcasm)


#utterance = sys.argv[1]
#rov = reverse_valence(utterance).capitalize()
#mostincongruent = rankContext(roberta,rov,'death','')
#sarcasm = rov + ' '+ mostincongruent
#f.write(sarcasm+'\n')
#print(sarcasm)



	
