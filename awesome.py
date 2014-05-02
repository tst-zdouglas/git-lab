#!/usr/bin/env python2.7
import random
import fileinput

print 'Hello world!'

print 'My name is Awesome; what\'s yours?'
for line in fileinput.input():
  print 'Nice to meet you %s' % line
  break

print 'I\'d like to play a game...'
attempts = 1000
while attempts and random.randint(0, 100) < 100 / 65:
  attempts -= 1
  print 'D'oh, keep guessing!'
