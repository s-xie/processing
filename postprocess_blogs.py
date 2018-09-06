import re
from nltk.tokenize import word_tokenize, sent_tokenize
from unidecode import unidecode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fin')
parser.add_argument('fout')
args = parser.parse_args()

def strip_html(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

sentences = set()
with open(args.fin, 'r', encoding='windows-1252') as f:
  count = 0
  for line in f:
    count+=1
    sentences.add(line.strip())

print('finished loading sentences')

count = 0
with open(args.fout, 'w') as f:
  group = ''
  for s in sentences:
    count+=1
    if s !='':
      group+=s+'\n'
      if count % 50==0:
        p = sent_tokenize(word_tokenize(unidecode(strip_html(group))))
        f.write('\n'.join(p))
        group = ''
    if count % 10000==0:
      print(count)
