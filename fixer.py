#!/usr/bin/python
# -*-  coding=utf-8

import sys
import tempfile
import subprocess
import os

replacements = [
  ['夢','歩'],
  ['蓮', '運'],
  ['軍','車'],
  ['魏','幼児'],
  ['蓮話', '運転'],
  ['藤装','服装'],
  ['脳装','服装'],
  ['単を','車を'],
  ['愛通','交通'],
  ['違肢','違反'],
  ['天型','大型'],
  ['必髪','必要'],
  ['勉許','免許'],
  ['銀鏡','眼鏡'],
  ['天切','大切'],
  ['証御書','証明書'],
  ['三輪車','二輪車'],
  ['同集者','同乗者'],
  ['藤ベルト','腰ベルト'],
]

def convert(line):
  for repl in replacements:
    line = line.replace(repl[0], repl[1])
  return line

def process(filename):
  print 'opening ' + filename
  fin = open(filename, 'r')
  fout = tempfile.NamedTemporaryFile('w', delete=False)
  
  for line in fin:
    fout.write(convert(line))
  fin.close()
  fout.close()
  diff_rv = subprocess.call('diff ' + filename + ' ' + fout.name, shell=True);
  if (diff_rv == 0):
    print 'nothing to change'
    return
  res = raw_input('Proceed?(y/n) ')
  if (res != 'y'):
    print 'abort'
    return
  os.rename(fout.name, filename)
  print 'updated: ' + filename

for line in sys.argv[1:]:
  process(line)
