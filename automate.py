#!/usr/bin/pyhton
import operator
import commands
import datanode
import namenode

c=commands.getstatusoutput("nmap -sP 192.168.56.0-255 -n | grep 'Nmap scan' |awk '{print $5}'")
y=open('b.txt',mode='wr')
y.write(c[1])
y.close()
fh=open('b.txt')

l=[]
for x in fh:
	if (x=='192.168.56.1\n' or (x=='192.168.56.100\n') or (x=='192.168.56.102')or (x=='192.168.56.101')):
		pass
	else:
		p=x.strip()
		l.append(p)
md=dict()
for x in l:
	if (x=='192.168.56.1\n' or x=='192.168.56.100\n' or x=='192.168.56.102' or x=='192.168.56.101'):
		pass
	else:
		g=commands.getstatusoutput("sshpass -p redhat ssh -l root "+x+" free -m |awk 'NR==2{print $2}'")		
		d=dict()
		d[x]=int(g[1])
		md.update(d)

md_list=sorted(md.items(),key=operator.itemgetter(1))

print md_list
print md_list[0][0]
#namenode.nn(md_list[0][0])
q=1
for i in md_list:
	if i==(md_list[0][0]):
		pass
	else:
		print md_list[q][0]
		datanode.dn(md_list[q][0])
		q=q+1











	
