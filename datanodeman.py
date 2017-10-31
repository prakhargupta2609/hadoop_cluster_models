#!/usr/bin/python

import os
import commands
def dn(s):
	cmd=" hostnamectl set-hostname data"
	commands.getstatusoutput("sshpass -p redhat ssh -l root {} {}".format(s,cmd))
	commands.getstatusoutput("sshpass -p redhat scp /root/Desktop/final_work/datanode/core-site.xml {}:/etc/hadoop/core-site.xml".format(s))
	commands.getstatusoutput("sshpass -p redhat scp /root/Desktop/final_work/datanode/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(s))
	service=" hadoop-daemon.sh start datanode"
	commands.getstatusoutput("sshpass -p redhat ssh -l root {} {}".format(s,service))

