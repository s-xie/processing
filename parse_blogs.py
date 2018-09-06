import glob
import xml.etree.ElementTree as ET
import re
import enchant
from textproc_utils import TextProc
from unidecode import unidecode
from HTMLParser import HTMLParser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('fout')
args = parser.parse_args()

h = HTMLParser()
textproc = TextProc()

parsed_file = open(args.fout, 'w')
for f_name in glob.glob("./data/*.xml"):
    res = re.search(r"male.([0-9]+).", f_name) 
    if (int(res.group(1)) < 20):
        continue
    print(f_name)
    with open(f_name, 'r') as f:
        contents = f.read()
        contents = unidecode(contents.decode('latin-1'))
        contents = h.unescape(contents)
        seek1 = contents.find('<post>')
        seek2 = contents.find('</post>', seek1+1)
        while(seek1!=-1):
            post = contents[seek1+6:seek2]
            try:
                sent_text=textproc.tokenizer.sent_tokenize(post) 
                for sent in sent_text:
                    parsed_file.write(sent.encode('latin-1')+"\n")
            except:
                print("tokenize error")
            seek1 = contents.find('<post>', seek1+1)
            seek2 = contents.find('</post>', seek1+1)
        f.close() 
