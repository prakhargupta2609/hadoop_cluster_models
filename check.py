#!/usr/bin/python
print "Content-Type: text/html"
print

import cgi
import datanodeman
import namenodeman

print "hi"

data= cgi.FormContent()
print data

print ((data['nn'][0]))
print ((data['jt'][0]))
print((data['dn'][0]))
print ((data['dn'][1]))
namenode.nn((data['nn'][0]))
datanode.dn((data['jt'][0]))
datanode.dn((data['dn'][0]))
datanode.dn((data['dn'][1]))

print "done"
