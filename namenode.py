#!/usr/bin/python

import os
def nn(s):
	cmd=" hostnamectl set-hostname namenode"
	os.system("sshpass -p redhat ssh -l root {} {}".format(s,cmd))
	os.system("sshpass -p redhat scp /root/Desktop/final_work/namenode/core-site.xml {}:/etc/hadoop/core-site.xml".format(s))
	os.system("sshpass -p redhat scp /root/Desktop/final_work/namenode/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(s))
	form=" hadoop namenode -format"
	service=" hadoop-daemon.sh start namenode"
	os.system("sshpass -p redhat ssh -l root {} {}".format(s,form))
	os.system("sshpass -p redhat ssh -l root {} {}".format(s,service))

