#!/usr/bin/python

import os
import commands
def nn(s):
	cmd=" hostnamectl set-hostname namenode"
	commands.getstatusoutput("sshpass -p redhat ssh -l root {} {}".format(s,cmd))
	commands.getstatusoutput("sshpass -p redhat scp /root/Desktop/final_work/namenode/core-site.xml {}:/etc/hadoop/core-site.xml".format(s))
	commands.getstatusoutput("sshpass -p redhat scp /root/Desktop/final_work/namenode/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(s))
	form=" hadoop namenode -format"
	service=" hadoop-daemon.sh start namenode"
	commands.getstatusoutput("sshpass -p redhat ssh -l root {} {}".format(s,form))
	commands.getstatusoutput("sshpass -p redhat ssh -l root {} {}".format(s,service))

