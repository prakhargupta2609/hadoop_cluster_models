#!/usr/bin/python

import os
def dn(s):
	cmd=" hostnamectl set-hostname datanode"
	os.system("sshpass -p redhat ssh -l root {} {}".format(s,cmd))
	os.system("sshpass -p redhat scp /root/Desktop/final_work/datanode/core-site.xml {}:/etc/hadoop/core-site.xml".format(s))
	os.system("sshpass -p redhat scp /root/Desktop/final_work/datanode/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(s))
	service=" hadoop-daemon.sh start datanode"
	os.system("sshpass -p redhat ssh -l root {} {}".format(s,service))

