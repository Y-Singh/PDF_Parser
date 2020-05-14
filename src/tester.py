import pdfminer.high_level
from . import __path__
print(__path__)
t = pdfminer.high_level.extract_text('PackSlips\\209721.pdf')
t=t.split('\n')
n = list()
for i in t:
    n.append(i + '<br>')
print(''.join(n))
