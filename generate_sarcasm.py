from reverse import reverse_valence
from retrieve import retrieveCommonSense
from rank import rankContext , getRoberta
import sys

roberta = getRoberta()

utterance = sys.argv[1]
rov = reverse_valence(utterance).capitalize()
op = retrieveCommonSense(utterance)
commonsense, extra = op[0], op[1]
mostincongruent = rankContext(roberta,rov,commonsense,extra)
sarcasm = rov + ' '+ mostincongruent
print(sarcasm)



	
