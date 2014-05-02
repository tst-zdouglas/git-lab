#!/usr/bin/env python2.7
import randoom
import fileinput

print 'Hello world!'

print 'My name is Awesome; what\'s yours?'
for line in fileinput.input():
  print 'Nice to meet you %s' % line
  break

print 'I\'d like to play a game...'
