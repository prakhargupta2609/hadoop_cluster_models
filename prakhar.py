#!/usr/bin/python
print "Content-Type: text/html"
print 

import os
import commands
import operator
import cgitb
import cgi

cgitb.enable()
c=commands.getstatusoutput("nmap -sP 192.168.56.0-255 -n | grep 'Nmap scan' |awk '{print $5}'")
print c
y=open('b.txt',mode='w')
y.write(c[1])
y.close()
fh=open('b.txt')

l=[]
for x in fh:
	if (x=='192.168.56.1\n' or (x=='192.168.56.100\n') or (x=='192.168.56.101')):
		pass
	else:
		p=x.strip()
		l.append(p)

md=dict()

for x in l:
	if (x=='192.168.56.1\n' or x=='192.168.56.100\n' or x=='192.168.56.101'):
		pass
	else:
		g=commands.getstatusoutput("sudo sshpass -p redhat ssh -l root "+x+" free -m |awk 'NR==2{print $2}'")		
		print g
		d=dict()
		d[x]=int (g[1])
		md.update(d)

md_list=sorted(md.items(),key=operator.itemgetter(1))
ind=0
cnt=1
for i in md_list:
	if cnt==1:
		print """<table border="1">
		 <th>IP OF SYSTEM</th>
		 <th>FREE-RAM </th>"""
	print """<tr>
		<td>%s </td>"""%md_list[ind][0]
	print """<td>%s</td>"""%md_list[ind][1]
	print """</tr>"""	
	cnt=cnt+1
	ind=ind+1

print """<form action='http://192.168.56.101/cgi-bin/check.py'>
	 Namenode-ip<input type="text" name='nn' /><br />
	 Job-Tracker<input type="text" name='jt' /><br />
      """
	
for i in range(0,(len(md_list)-2),1):
	print """Datanode<input type="text" name='dn'/><br/>"""
print """<input type="submit" /></form>"""








