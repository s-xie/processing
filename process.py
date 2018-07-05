import re
import sys
from nltk.tokenize import word_tokenize
from unidecode import unidecode
from nltk.tokenize import sent_tokenize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fin')
parser.add_argument('fout')
args = parser.parse_args()

textproc = TextProc()
tokenizer = Tokenizer()

sentences=set()
with open(args.fin, 'r') as f:
  count = 0
  for line in f:
    count+=1
    sentences.add(line.strip())
    if count % 100000==0:
        print(count)


with open(args.fout, 'w') as f:
  count = 0
  group = ''
  for s in sentences:
    count+=1
    if s !='':
      group+=s+'\n'
      if count % 20==0:
        try:
          p = sent_tokenize(unidecode(group))
          f.write('\n'.join(p))
          group = ''
        except:
          print("nltk error")
    if count % 10000==0:
        print(count)
