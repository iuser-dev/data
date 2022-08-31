#!/usr/bin/env python

from lang_hs2chrome import HS2CHROME
from os.path import dirname, abspath, join
from json import dumps

ROOT = dirname(dirname(dirname(abspath(__file__))))


def file_to_dict(fp):
  d = {}
  with open(fp) as f:
    for i in f:
      i = i.strip()
      if i:
        key, val = i.split(' ', 1)
        d[key] = val
  return d


locate = file_to_dict('./lang.locate.txt')
hs = file_to_dict('./google.txt')

li = []

for i in hs:
  key = HS2CHROME.get(i, i)
  if key in locate:
    li.append((key, locate[key]))

with open('./lang.ord.txt') as order:
  order = list(map(str.strip, order))

#li.append(('zh-TW', '正體中文'))
li.sort(key=lambda x: (order + [x[0]]).index(x[0]))

with open(join(ROOT, 'ui/src/i18n/lang.coffee'), 'w') as out:
  out.write('export default "' + '|'.join('|'.join(i) for i in li) + '"')

li = []
for i in hs:
  key = HS2CHROME.get(i, i)
  if key in locate:
    li.append(key)

with open(join(ROOT, 'i18n/i18n/src/lang_li.coffee'), 'w') as out:
  out.write('export default ' + dumps(li) )
