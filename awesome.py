#!/usr/bin/env python2.7
import random
import fileinput

print 'Hello world!'

print 'My name is Awesome; what\'s yours?'
for line in fileinput.input():
  print 'Nice to meet you %s' % line
  break

print 'I\'d like to play a game...'
MAX_ATTEMPTS = 1000
MIN_INT = 0
MAX_INT = 100
PRB = 65
attempts = MAX_ATTEMPTS
while attempts and random.randint(MIN_INT, MAX_INT) < PRB:
  attempts -= 1
  print 'Doh, keep guessing!'
