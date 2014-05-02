#!/usr/bin/env python2.7
import fileinput

print 'Hello world!'

print 'My name is Awesome; what\'s yours?'
for line in fileinput.input():
  print 'Nice to meet you %s' % line
  break
