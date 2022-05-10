import json
from collections import defaultdict

with open('../../data/processed/test.json') as file:
    data = [json.loads(l) for l in file.readlines()]

gold = defaultdict(list)
pred = defaultdict(list)
for i, d in enumerate(data):
    sentences = []
    sent = []
    prev = None
    for j in range(len(d['tokens'])+1):
        if j == len(d['tokens']) or d['tokens'][j] == '<SENT>':
            if len(sent) > 0:
                sentences.append(sent)
                if '?' in sent[-1]:
                    if prev != 'O':
                        pred['I_QUESTION'].append((i,len(sentences)-1))
                        prev = 'I_QUESTION'
                    else:
                        pred['B_QUESTION'].append((i,len(sentences)-1))
                        prev = 'B_QUESTION'
                else:
                    prev = 'O'
            if j < len(d['tokens']) and d['labels'][j] != 'O':
                gold[d['labels'][j]].append((i,len(sentences)))
            sent = []
        else:
            sent += [d['tokens'][j]]

print(gold.keys())
print(pred.keys())

precs = []
recs = []
f1s = []
for k in gold.keys():
    if k in pred:
        correct = 0
        for p in pred[k]:
            if p in gold[k]:
                correct += 1
        prec = correct / len(pred[k])
        rec = correct / len(gold[k])
        f1 = 2*prec*rec/(prec+rec)
        precs += [prec]
        recs += [rec]
        f1s += [f1]
        print('precision ('+k+') : ', prec)
        print('recall ('+k+') : ', rec)
        print('f1 ('+k+') : ', f1)
        print('-'*10)

prec = sum(precs)/len(precs)
rec = sum(recs)/len(recs)
print('precision: ', prec)
print('recall: ', rec)
print('F1: ', 2*prec*rec/(prec+rec))
